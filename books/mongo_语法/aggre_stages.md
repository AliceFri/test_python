#### $addFields 向文档添加新字段
{ $addFields: { <newField>: <expression>, ... } }

{ $addFields: { totalScore:{ $add: [ "$totalHomework", "$totalQuiz", "$extraCredit" ] } } }
// 添加嵌入文档字段
{ $addFields: {"specs.fuel_type": "unleaded"} }
// 添加数组元素
{ $addFields: { homework: { $concatArrays: [ "$homework", [ 7 ] ] } } }

#### $bucket 桶分组
{
    $bucket: {
      groupBy: "$year_born",                        // Field to group by
      boundaries: [ 1840, 1850, 1860, 1870, 1880 ], // Boundaries for the buckets
      default: "Other",                             // Bucket id for documents which do not fall into a bucket
      output: {                                     // Output for each bucket
        "count": { $sum: 1 },
        "artists" :
          {
            $push: {
              "name": { $concat: [ "$first_name", " ", "$last_name"] },
              "year_born": "$year_born"
            }
          }
      }
    }
}

#### $count 计算文档数量
{ $count: <string> }

{ $count: "myCount" }


#### $group 分组
{
  $group:
    {
      _id: <expression>, // Group By Expression
      <field1>: { <accumulator1> : <expression1> },
      ...
    }
 }

// 计算文档数量
{ $group: { _id: null, count: { $sum: 1 } } }

// 检索不同的值
{ $group : { _id : "$item" } }

// Group by Item Having
    // First Stage
    {
      $group :
        {
          _id : "$item",
          totalSaleAmount: { $sum: { $multiply: [ "$price", "$quantity" ] } }
        }
     },
    // Second Stage
     {
       $match: { "totalSaleAmount": { $gte: 100 } }
     }

// 按日期分组
{ $group : {_id : { $dateToString: { format: "%Y-%m-%d", date: "$date" } }} }

// 分组，组合列表
{ $group : { _id : "$author", books: { $push: "$title" } } }


#### $limit 限制输出
{ $limit: <number> }


#### $lookup 关联查询
{
   $lookup:
     {
       from: <collection to join>,
       localField: <field from the input documents>,
       foreignField: <field from the documents of the "from" collection>,
       let: { <var_1>: <expression>, …, <var_n>: <expression> },
       pipeline: [ <pipeline to run> ],
       as: <output array field>
     }
}

{
     $lookup:
       {
         from: "inventory",
         localField: "item",
         foreignField: "sku",
         as: "inventory_docs"
       }
  }

// Use $lookup with an Array
{
      $lookup:
         {
            from: "members",
            localField: "enrollmentlist",   # array
            foreignField: "name",
            as: "enrollee_info"
        }
   }

// Use $lookup with $mergeObjects
{
      $lookup: {
         from: "items",
         localField: "item",    // field in the orders collection
         foreignField: "item",  // field in the items collection
         as: "fromItems"
      }
},
{
    $replaceRoot: { newRoot: { $mergeObjects: [ { $arrayElemAt: [ "$fromItems", 0 ] }, "$$ROOT" ] } }
}


#### $match 匹配
{ $match : { author : "dave" } }
{ $match: { $or: [ { score: { $gt: 70, $lt: 90 } }, { views: { $gte: 1000 } } ] } }

...