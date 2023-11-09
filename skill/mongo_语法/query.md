#### 1. 检索集合中所有的文档

db.collection.find({})

##### 1.1 等值查询
{<field>: <value>, ...}

db.inventory.find( { status: "D" } )

##### 1.2 查询操作符

db.inventory.find( { status: { $in: [ "A", "D" ] } } )

==Comparison==
$eq: 等于        { <field>: { $eq: <value> } }
                db.inventory.find( { qty: { $eq: 20 } } )
                db.inventory.find( { qty: 20 } )
                db.inventory.find( { tags: "B" } )  # 可用于数组， 如果tags包含B

$gt: 大于        { <field>: { $gt: <value> } }
$gte: 大于等于    { <field>: { $gte: <value> } }
$lt: 小于        { <field>: { $lt: <value> } }
$lte: 小于等于    { <field>: { $lte: <value> } }

$in: 在列表中     { <field>: { $in: [ <value>, ... ] } }
                db.inventory.find( { tags: { $in: [ /^be/, /^st/ ] } } )
                db.inventory.find({ tags: { $in: ["appliances", "school"] } })
$ne: 不等于      { <field>: { $ne: <value> } }
$nin: 不在列表中 { <field>: { $nin: [ <value>, ... ] } }

==Logical==

$and: 并且        { <field>: { $and: [ <value>, ... ] } }
$not: 非          { <field>: { $not: <value> } }
$or: 或          { <field>: { $or: [ <value>, ... ] } }
$nor: 或非        { <field>: { $nor: [ <value>, ... ] } } 

db.inventory.find( {
    $and: [
        { $or: [ { qty: { $lt : 10 } }, { qty : { $gt: 50 } } ] },
        { $or: [ { sale: true }, { price : { $lt : 5 } } ] }
    ]
} )
db.inventory.find( { item: { $not: { $regex: /^p.*/ } } } )


==Element==

$exists: 字段是否存在 { <field>: { $exists: <bool> } }
            db.inventory.find( { qty: { $exists: true, $nin: [ 5, 15 ] } } )

$type: 字段类型    { <field>: { $type: <type> } }
            db.addressBook.find( { "zipCode" : { $type : 1 } } )
            db.addressBook.find( { "zipCode" : { $type : "double" } } )


==Evaluation==

$expr: 表达式      { <field>: { $expr: <value> } }
    db.monthlyBudget.find( { $expr: { $gt: [ "$spent" , "$budget" ] } } )

$jsonSchema: 校验     { <field>: { $jsonSchema: <value> } }
$mod: 模数          { <field>: { $mod: [ <divisor>, <remainder> ] } }
$regex: 正则表达式  { <field>: { $regex: <value> } }
$text: 文本搜索     { <field>: { $text: <value> } }
$where: 条件        { <field>: { $where: <value> } }

    db.players.find( { $where: function() {
        return (hex_md5(this.name) == "9b53e667f30cd329dca1ec9e6a83e994")
    } } );


==Geospatial==

==Array==

$all: 所有         { <field>: { $all: [ <value>, ... ] } }
$elemMatch: 匹配元素 { <field>: { $elemMatch: <value> } }
            列表中只要有一个元素匹配，则匹配

$size: 列表大小     { <field>: { $size: <value> } }


==Bitwise==

==Comments==

----------------------------

### 2. 查询文档中的某个字段

除_id字段外，不能在映射文档中同时使用包含和去除语句。
db.inventory.find( { status: "A" }, { item: 1, status: 1 } )

通过点号引用嵌套文档字段并且在映射文档中将该字段设置为1来实现返回嵌套文档中的指定字段。(数组)
db.inventory.find(
   { status: "A" },
   { item: 1, status: 1, "size.uom": 1 }
)

通过点号引用嵌套文档字段并且在映射文档中将该字段设置为0来实现去除嵌套文档中的指定字段。
db.inventory.find(
   { status: "A" },
   { "size.uom": 0 }
)

下面的案例使用$slice映射操作符返回数组字段instock中最后的元素:
db.inventory.find( { status: "A" }, { item: 1, status: 1, instock: { $slice: -1 } } )

----------------------------

### 3. 查询嵌入式文档数组

# 不关心warehouse 和 qty 顺序
db.inventory.find( { "instock": { warehouse: "A", qty: 5 } } )
# 关心warehouse 和 qty 顺序
db.inventory.find( { "instock": { qty: 5, warehouse: "A" } } )

返回instock数组中最少有一个嵌套文档包含字段qty的值小于等于20的所有文档 :
db.inventory.find( { "instock": { $elemMatch: { qty: { $lte: 20 } } } } )

返回instock数组中的第一个元素是包含字段qty小于等于20的文档的所有文档
db.inventory.find( { 'instock.0.qty': { $lte: 20 } } )


----------------------------

### 4. 查询数组

# 等值查询
db.inventory.find( { tags: ["red", "blank"] } )

