### 1. 全局锁

    flush tables with read lock

    unlock tables

    锁数据库； 当会话断开了，全局锁会被自动释放；

----

### 2. 表级锁
    
#### 表锁  读/写
    lock tables t_student read;
    lock tables t_student write;

    表锁 除了限制别的线程，也会限制本线程接下来的读写操作；

#### 元数据锁 MDL 读/写

    不需要显式调用， 会自动加锁；自动上锁/解锁 事务提交后才会释放；

    MDL 是写优先锁；

#### 意向锁
    给 行上S 独占锁， 需要给 表级别加 一个 意向独占锁；
    给 行上W 共享锁， 需要给 表级别加 一个 意向共享锁；

    普通的select语句并不加锁，是无锁的；update, insert, delete需要加写锁；

    select ... lock in share mode;  会加共享锁
    select ... for update;          会加独占锁

    意向共享锁和意向独占锁是表级锁，不会和行级的共享锁和独占锁发生冲突，而且意向锁之间也不会发生冲突，
    只会和共享表锁（lock tables ... read）和独占表锁（lock tables ... write）发生冲突。

    意向锁的目的是为了快速判断表里是否有记录被加锁。

#### AUTO-INC 锁

    自增锁， 表锁； 执行完插入语句后就会立即释放。

    更轻量级的锁： 然后给该字段赋值一个自增的值，就把这个轻量级锁释放了，而不需要等待整个插入语句执行完后才释放锁。

    当 innodb_autoinc_lock_mode = 2 时，并且 binlog_format = row，既能提升并发性，又不会出现数据一致性问题。

-------

### 3. 行级锁

#### 3.1 记录锁 record lock

    锁住的是一条记录
    select ... lock in share mode;  会加共享锁
    select ... for update;          会加独占锁

#### 3.2 间隙锁 Gap Lock
    间隙锁虽然存在 X 型间隙锁和 S 型间隙锁，但是并没有什么区别，间隙锁之间是兼容的，即两个事务可以同时持有包含共同间隙范围的间隙锁，
    并不存在互斥关系，因为间隙锁的目的是防止插入幻影记录而提出的。

#### 3.3 临键锁 Next-Key Lock

    next-key lock 是包含间隙锁+记录锁的，如果一个事务获取了 X 型的 next-key lock，
    那么另外一个事务在获取相同范围的 X 型的 next-key lock 时，是会被阻塞的。

#### 3.4 插入意向锁
    
    一个点的特殊的间隙锁， 明有事务想在某个区间插入新记录，但是现在处于等待状态。