### 插入记录

存储在集合中的每个文档都需要一个唯一的**_id字段作为主键。 如果插入的文档省略_id字段，
则MongoDB驱动程序会自动为_id字段生成ObjectId**

##### db.collection.insertOne(document)

db.inventory.insertOne(  
        { item: "canvas", qty: 100, tags: ["cotton"], size: { h: 28, w: 35.5, uom: "cm" } }
)

##### db.collection.insertMany(documents)

------

##### upsert: true




