BASE_PIPELINE = [
    {
        "$set": {
            "id": "$_id",
        }
    },
    {
        "$unset": "_id",
    },
]

# delete_rule
DELETE_RULE_NONE = 0
DELETE_RULE_CASCADE = 1
DELETE_RULE_SET_NULL = 2
DELETE_RULE_PULL = 3    # 删除时，将引用类型的字段(列表)弹出该值
