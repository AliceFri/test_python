### 更新单个文档

    db.collection.update({'_id': ObjectId('5b8f8f8f8f8f8f8f8f8f8f8')}, {'$set': {'name': '小明'}})

    db.inventory.updateOne(
        { item: "paper" },
        {
            $set: { "size.uom": "cm", status: "P" }, 
            $currentDate: { lastModified: true }
        }
    )

### 更新多个文档

  db.inventory.updateMany( 
      { "qty": { $lt: 50 } },
      {  
          $set: { "size.uom": "in", status: "P" }, 
          $currentDate: { lastModified: true }  
      }
  )
  
### 更换文档

    db.inventory.replaceOne(
        { item: "paper" },
        { item: "paper", instock: [ { warehouse: "A", qty: 60 }, { warehouse: "B", qty: 40 } ] }
    )

### 聚合管道更新

# $addFields
    {
     $addFields: {
       totalHomework: { $sum: "$homework" } ,
       totalQuiz: { $sum: "$quiz" }
     }
   },

# $project (投影)
db.books.aggregate( [ { $project : { title : 1 , author : 1 } } ] )
    
# 聚合管道 $$NOW $set 用法
db.students.updateOne( { _id: 3 }, [ { $set: { "test3": 98, modified: "$$NOW"} } ] )

# $unset 删除字段
{ $unset: [ "<field1>", "<field2>", ... ] }

# $replaceRoot

db.people.aggregate( [
   { $replaceRoot: { newRoot: { $mergeObjects:  [ { dogs: 0, cats: 0, birds: 0, fish: 0 }, "$pets" ] }} }
] )

$replaceRoot: {
         newRoot: {
            full_name: {
               $concat : [ "$first_name", " ", "$last_name" ]
            }
         }
      }

