#### gorm.Model
    包含了 ID, CreatedAt, UpdatedAt, DeletedAt 这几个字段

#### 字段级权限控制
    Name string `gorm:"<-:create"` // 允许读和创建 
    ...

#### 创建/更新时间追踪
    GORM 约定使用 CreatedAt、UpdatedAt 追踪创建/更新时间。如果您定义了这种字段，GORM 在创建、更新时会自动填充
    要使用不同名称的字段，您可以配置 autoCreateTime、autoUpdateTime 标签。
    想要保存 UNIX（毫/纳）秒时间戳，而不是 time，您只需简单地将 time.Time 修改为 int 即可

-----------


### Create
    // 通过数据的指针来创建 单条记录
    user := User{Name: "Jinzhu", Age: 18, Birthday: time.Now()}
    result := db.Create(&user) // 通过数据的指针来创建; user.ID 返回数据的主键  result.Error 返回error result.RowsAffected 返回记录数
    // 传递切片以插入多行数据, 批量插入
    users := []*User{User{Name: "Jinzhu", Age: 18, Birthday: time.Now()}, User{Name: "Jinzhu", Age: 18, Birthday: time.Now()}}
    result := db.Create(users)
    // db.CreateInBatches(users, 100) 可以设置 batch size

    // 指定字段创建
    db.Select("Name", "Age", "CreatedAt").Create(&user)
    db.Omit("Name", "Age", "CreatedAt").Create(&user)
    
    // 根据map创建, 钩子不会触发, 主键不会回填
    db.Model(&User{}).Create([]map[string]interface{}{
        {"Name": "jinzhu_1", "Age": 18},
        {"Name": "jinzhu_2", "Age": 20},
    })
    
    // 使用 map, 自定义类型 实现SQL表达式 创建记录

    // 关联创建
    db.Create(&User{
        Name: "jinzhu",
        CreditCard: CreditCard{Number: "411111111111"}
    })
    // INSERT INTO `users` ...
    // INSERT INTO `credit_cards` ...
    // skip insert credit_cards
    db.Omit("CreditCard").Create(&user) 
    // skip all associations
    db.Omit(clause.Associations).Create(&user)

    // UpsertCreate 设置 OnConflict   (没有有则创建，有则更新，支持批量)

### Query
    
    // 检索单个对象 db.First(&user)  避免db.Find(&user)单个对象使用Find而不带limit
    First Take Last  且没有找到记录时，它会返回 ErrRecordNotFound 错误,如果model没有主键,按 model 的第一个字段进行排序。

    // 根据主键搜索
    // 主键是数字类型， 可以使用 内联条件
    db.First(&user, 10)   db.Find(&users, []int{1,2,3})
    // 非数字类型
    db.First(&user, "id = ?", "1b74413f-f3b8-409f-ac47-e8c062e3472a")

    // 条件查询
    db.Where("name = ?", "jinzhu").First(&user)
    db.Where("name IN ?", []string{"jinzhu", "jinzhu 2"}).Find(&users)
    db.Where("name LIKE ?", "%jin%").Find(&users)
    db.Where("name = ? AND age >= ?", "jinzhu", "22").Find(&users)
    db.Where("created_at BETWEEN ? AND ?", lastWeek, today).Find(&users)
    // struct map 条件 When querying with struct, GORM will only query with non-zero fields
    db.Where(&User{Name: "jinzhu"}, "name", "Age").Find(&users) // 可以指定结构体查询字段，或者使用map    

    // Query conditions can be inlined into methods like First and Find in a similar way to Where.

    // Not条件 Or条件 not works similar to Where
    db.Not("name = ?", "jinzhu").First(&user)
    db.Where("role = ?", "admin").Or("role = ?", "super_admin").Find(&users)

    // 选择特定字段
    db.Select("name", "age").Find(&users)

    // 排序
    db.Order("age desc, name").Find(&users)

    // LIMIT / OFFSET
    db.Limit(10).Offset(5).Find(&users)

    // DISTINCT
    db.Distinct("name", "age").Order("name, age desc").Find(&results)

    // JOINS
    db.Model(&User{}).Select("users.name, emails.email").Joins("left join emails on emails.user_id = users.id").Scan(&result{})
    db.Joins("Company").Find(&users)
    db.InnerJoins("Company").Find(&users)

    // Scan Scanning results into a struct works similarly to the way we use Find； FIND 是 into * struct

### High Query

    // 智能选择字段, 自动填充 APIUser  
    db.Model(&User{}).Limit(10).Find(&APIUser{})

    // 锁

    // 子查询
    db.Where("amount > (?)", db.Table("orders").Select("AVG(amount)")).Find(&orders)
    // SELECT * FROM "orders" WHERE amount > (SELECT AVG(amount) FROM "orders");
    db.Table("(?) as u", db.Model(&User{}).Select("name", "age")).Where("age = ?", 18).Find(&User{})
    // SELECT * FROM (SELECT `name`,`age` FROM `users`) as u WHERE `age` = 18
    subQuery1 := db.Model(&User{}).Select("name")
    subQuery2 := db.Model(&Pet{}).Select("name")
    db.Table("(?) as u, (?) as p", subQuery1, subQuery2).Find(&User{})
    // SELECT * FROM (SELECT `name` FROM `users`) as u, (SELECT `name` FROM `pets`) as p 

    // 多个列的IN
    db.Where("(name, age, role) IN ?", [][]interface{}{{"jinzhu", 18, "admin"}, {"jinzhu2", 19, "user"}}).Find(&users)
    // SELECT * FROM users WHERE (name, age, role) IN (("jinzhu", 18, "admin"), ("jinzhu 2", 19, "user"));

    // FIND 至 map. 需要指定Model, Table
    
    FirstOrInt 获取第一条匹配的记录， 未找到则初始化一条记录（并不会存到数据库）
    db.Where(User{Name: "non_existing"}).Attrs(User{Age: 20}).FirstOrInit(&user)
    Assign都会将属性赋值，不会用于查询，也不会保存到数据库

    FirstOrCreate 获取第一条匹配的记录， 未找到则创建一条记录 
    Attr, 不用于查询，找到了则忽略，未找到则保存到数据库，赋值
    Assign 不用于查询，找到了赋值，未找到保存到数据库，赋值

    // 优化器，索引提示

    // 迭代

    // FindInBatches 批量查询并处理记录

    Pluck  用于查询单个列，并扫描到切片

    Scope 复用查询条件

    Count 获取匹配的记录数

### Update

    // 保存所有字段 有就更新，没有就保存（只限于主键）
    Save 会保存所有字段，即使字段是零值。 有主键则执行Update, 没有则执行Create。 Save不要搭配Model使用。

    // 更新单个列
    db.Model(&User{}).Where("active = ?", true).Update("name", "hello")
    // UPDATE users SET name='hello', updated_at='2013-11-17 21:34:10' WHERE active=true;

    // 更新多列 when updating with struct it will only update non-zero fields by default
    db.Model(&user).Updates(User{Name: "hello", Age: 18, Active: false})

    // 更新选定字段 Seltct Omit

    // 默认阻止全局更新

    // 根据子查询进行更新
    db.Model(&user).Update("company_name", db.Model(&Company{}).Select("name").Where("companies.id = users.company_id"))
    // UPDATE "users" SET "company_name" = (SELECT name FROM companies WHERE companies.id = users.company_id);

### Delete
    
    // 删除一条记录
    // Email 的 ID 是 `10`
    db.Delete(&email)
    // DELETE from emails where id = 10;

    // 带条件的删除
    db.Where("name = ?", "jinzhu").Delete(&email)
    db.Delete(&email, conds...)

    // 软删除 DeletedAt