db.inventory.aggregate([{}])

### 阶段

$addFields $set 向文档添加新字段
{"$addFields": {"a": "$status"}}    # 将status字段添加到新字段中，并命名为a

$count 计算文档数量
{"$count": "count"}

$group 分组
{"$group": {"_id": "$status", "count": {"$sum": 1}}}    # 按status分组，计算每组的文档数量

$limit 限制输出数量
{"$limit": 10}

$skip 跳过前n条文档
{"$skip": 10}

$lookup 关联查询
{"$lookup": {"from": "categories", "localField": "category", "foreignField": "_id", "as": "categories"}}    # 关联categories表，查询category字段对应的categories表的_id字段，并命名为categories

$match 查询条件
{"$match": {"status": "A"}}    # 查询status字段为A的文档
{'$match': {'$or': [{'_id': try_oid(resource_id)}, {'hostname': resource_id}]}}

$project 选择字段
{"$project": {"name": 1, "status": 1}}    # 只选择name和status字段

$replaceRoot 替换根节点
{"$replaceRoot": {"newRoot": "$categories"}}    # 替换根节点为categories表的文档

$sort 排序
{"$sort": {"name": 1}}    # 按name字段升序排序

$unset 删除字段
{"$unset": {"name": 1}}    # 删除name字段

$unwind 分割数组
{"$unwind": "$categories"}    # 将categories字段分割成文档，并命名为categories


### 聚合变量
$$NOW 当前时间  {$set: {"now": "$$NOW"}}


### 表达式

----------- 算数表达式运算符 -----------

$abs 绝对值  {"$abs": "$price"}
$add 加法  {"$add": ["$price", "$tax"]}
$ceil 向上取整  {"$ceil": "$price"}

