### 1. Maxmemory 设置

    1. redis.conf   maxmemory 100mb
    2. CONFIG SET 运行时设置


### 2. 淘汰策略

    maxmemory-policy

    noeviction: 不淘汰, 内存满时, 不保存新数据
    allkeys-lru: 保留最近使用的数据
    allkeys-lfu: 保留最常使用的数据
    volatile-lru: 保留最近使用的数据, 移出有expire的数据
    volatile-lfu: 保留最常使用的数据, 移出有expire的数据
    allkeys-random
    volatile-random
    volatile-ttl

The policies volatile-lru, volatile-lfu, volatile-random, and volatile-ttl behave like noeviction if there are no keys to evict matching the prerequisites.

==运行时可更改淘汰策略, INFO可查看缓存命中率==

### 3. 淘汰进程如何工作

    增加数据时，检查是否超出上限，若超出上限，则根据策略选出淘汰的键淘汰。

    所以可能会有超出上限的时刻存在。
    

### 4. 近似的LRU算法

    maxmemory-samples 5。 淘汰一系列键中最该被淘汰的， 近似LRU

However, the approximation is virtually equivalent for an application using Redis. This figure compares the LRU approximation used by Redis with true LRU.


### 5. LFU算法

    Morris计数器， 用很小的数据结构，准确估计数据技术
    近似计数算法，它不是提供精确计数，而是提供一个近似计数
    节约空间
