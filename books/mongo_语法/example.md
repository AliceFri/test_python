# mongo db
表为plan， 字段为user, name

# 索引
db.getCollection("plan").getIndexes()
db.getCollection("plan").dropIndex("name_1") 

# 修改plan的name字段
db.getCollection("plan").find().forEach(
    function(item){
        db.getCollection("plan").update({"_id": item._id}, {"$set": {"name": item.name}}, false, true)
    }
)


# 修改字段为默认值
db.getCollection("plan").updateMany(
    {},
    {
        "$set": {"name": "default_name"}
    }
)

# 删除某个字段Field
db.getCollection("plan").update({}, {$unset: {"name": ""}}, false, true)

# 查询 时间，正则
db.getCollection("plan").find({
    update_datetime: {$gt: new ISODate('2022-04-19')},
    method: 'POST',
    url: {$regex: 'api/ope'}
})

# 将某个字段改成列表 7:ObjectID 4: Array
db.getCollection("plan").updateMany(
{user: {$ne: null, $type: 7, $not: {$type: 4}}}, [{$set:{user:["$user"]}}])

# 根据表中某个字段生成新字段

db.getCollection("parkablecurbs").find().forEach(
    function(item){
        j = {type: 'LineString', coordinates: []};
        for (i of item.polyline){
            j.coordinates.push([i.lon, i.lat]);
        }
        db.getCollection("plan").update({"_id": item._id}, {"$set": {"geolinestring": j}}, false, true)
    }
)

db.getCollection("vehicle").find({hostname: / /}).forEach(function(item) {
    h = item.hostname.trim();
    db.getCollection("vehicle").update({"_id": item._id}, {$unset: {"hostname": ""}, "$set": {"hostname": h}})
}) 

62c4ca45e0e78a0e155333b2
6302e15ff50dfef02c5bdb3d
6302e1b3f1d189311b88b3c9
62a010d4260b2888740acf37












### lookup

1. 设置为第一个
    {
        '$lookup': {
            'from': 'plan',
            'localField': 'plan',
            'foreignField': '_id',
            'as': 'location',
        },
    },
    {
        '$set': {
            'plan': {'$first': '$plan.name'},
        }
    },