### Strings

最基本的数据类型， 二进制安全， 可以包含任何类型的数据。例如JPEG等

最大512MB

https://redis.io/commands/?group=string
String能做很多有趣的事：
    1. INCR family: INCR, DECR, INCRBY

    2. APPEND

    3. SETRANGE, GETRANGE

    4. GETBIT SETBIT

AllCommands:

APPEND key value
DECR key
DECRBY key decrement
GET key
GETDEL key
GETEX key seconds
GETRANGE key start end
GETSET key value
INCR key
INCRBY key increment
INCRBYFLOAT key increment
LCS key1 key2
MGET key [key ...]
MSET key value [key value ...]
MSETNX key value [key value ...]
PSETEX key milliseconds value
SET key value [EX seconds] [PX milliseconds] [NX|XX]
SETNX key value
SETEX key seconds value
SETRANGE key offset value
STRLEN key
SUBSTR key start end


### Lists

Lists 是简单的strings列表， 按照插入顺序排列。
LPUSH key value [value ...]
RPUSH key value [value ...]
key不存在会创建一个空的list， list为空时会删除key。

Interesting things:
    1. LPUSH  配合 LRANGE 获取一段时间的数据
    2. LPUSH  配合 LTRIM 只保留最新的N条数据
    3. blocking commands like BLPOP, BRPOP

BLPOP key [key ...] timeout
BRPOP key [key ...] timeout
BRPOPLPUSH source destination timeout
LINDEX key index
LINSERT key BEFORE|AFTER pivot value
LLEN key
LMOVE source destination index
LMPOP key [key ...] timeout
LPOP key
LPUSH key value [value ...]
LPUSHX key value
LRANGE key start stop
LREM key count value
LSET key index value
LTRIM key start stop


### Sets

无顺序的string集合，支持服务器端的并集，交集，差集等操作。

最大的数量是 2 ^ 32 - 1

    1. SADD key member [member ...]
    2. SINTER
    3. SPOP

SADD key member [member ...]
SCARD key   # 返回集合的成员数量
SDIFF key [key ...] # 返回集合的差集
SDIFFSTORE destination key [key ...] # 返回集合的差集 并存储到 destination
SINTER key [key ...] # 返回集合的交集
SINTERSTORE destination key [key ...] # 返回集合的交集 并存储到 destination
SINTERCARD key [key ...] # 返回集合的交集的成员数量
SISMEMBER key member # 判断 member 是否是 key 的成员
SMEMBERS key # 返回集合的所有成员
SMISMEMBER key member # 判断 多个member 是否不是 key 的成员
SMOVE source destination member # 将 member 移动到 destination 集合
SPOP key # 移除并返回集合中的一个随机元素
SRANDMEMBER key # 返回集合中的一个随机元素
SREM key member [member ...] # 移除集合中的一个或多个元素
SSCAN key cursor [MATCH pattern] [COUNT count] # 迭代集合中的元素
SUNION key [key ...] # 返回集合的并集
SUNIONSTORE destination key [key ...] # 返回集合的并集 并存储到 destination


### Hashes
    
    完美的表示对象的数据类型 

        HMSET user:1000 username antirez password P1pp0 age 34
        HGETALL user:1000
        HSET user:1000 password 12345
        HGETALL user:1000

HDEL key field [field ...]  # 删除一个或多个item
HEXISTS key field # 判断 field 是否存在
HGET key field # 返回 value
HGETALL key # 返回所有的field和value
HINCRBY key field increment # 增加field的值
HINCRBYFLOAT key field increment # 增加field的值
HKEYS key # 返回所有的field
HLEN key # 返回 field的数量
HMGET key field [field ...] # 返回所有的field的value
HMSET key field value [field value ...] # 设置一个或多个field的value
HRANDFIELD key # 返回一个随机的field
HSCAN key cursor [MATCH pattern] [COUNT count] # 迭代所有的field和value
HSET key field value # 设置一个field的value
HSETNX key field value # 设置一个field的value，如果不存在则设置成功
HSTRLEN key field # 返回field的value的长度
HVALS key # 返回所有的field的value

### Sorted Sets

    与set一样 非重复strings的集合，按照score从小到大排列。
    可以按分数来获取元素
    很适合用来做排行榜

    1. ZADD ZRANGE ZRANK
    2. 用户id 作为value， age作为分数， 能快速获取不同年龄段的用户， ZRANGEBYSCORE