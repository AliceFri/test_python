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