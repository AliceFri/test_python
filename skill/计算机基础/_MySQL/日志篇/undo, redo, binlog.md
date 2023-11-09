### 1. undo log
    回滚日志， 实现了事务 中的原子性， 主要用于事务回滚和MVCC

    增删改语句时， 单条语句，mysql也是会隐式开启事务； 执行一条语句是否自动提交事务，是由autocommit参数决定的；

    undo log 是一种用于撤销回退的日志。在事务没提交之前，MySQL 会先记录更新前的数据到 undo log 日志文件里面，
    当事务回滚时，可以利用 undo log 来进行回滚

    插入一条记录， undo 日志记录下主键值， 回滚时进行删除操作；
    删除一条记录， undo 日志记录下该记录， 回滚时进行插入操作；
    更新一条记录， undo 日志记录下更新前的旧值， 回滚时进行更新操作；

    一条记录的每一次更新操作产生的 undo log 格式都有一个 roll_pointer 指针和一个 trx_id 事务id；

    
    undolog 两大作用：
        1. 实现事务的原子性，实现事务回滚
        2. 实现MVCC（多版本并发控制） 关键元素之一

### 1.1 undo log 的 持久化
    
    buffer pool 中 有undo页， undo页的修改会记录到redo log ； redo log会每秒刷盘，提交事务时也会刷盘；

    数据页和undo页都是靠这个机制保证持久化的；

----

### 2. Buffer Pool 缓冲池 (基于内存)

    当读取数据时，如果数据存在于 Buffer Pool 中，客户端就会直接读取 Buffer Pool 中的数据，否则再去磁盘中读取。

    当修改数据时，如果数据存在于 Buffer Pool 中，那直接修改 Buffer Pool 中数据所在的页，
    然后将其页设置为脏页（该页的内存数据和磁盘上的数据已经不一致），
    为了减少磁盘I/O，不会立即将脏页写入磁盘，后续由后台线程选择一个合适的时机将脏页写入到磁盘。

    以页为单位： 数据页， 索引页， undo页, 锁信息...

----

### 3. redo log (重做日志)

    WAL： write-ahead logging MySQL 的写操作并不是立刻写到磁盘上，而是先写日志，然后在合适的时间再写到磁盘上。

    redo log 是物理日志，记录了某个数据页做了什么修改，
    比如对 XXX 表空间中的 YYY 数据页 ZZZ 偏移量的地方做了AAA 更新，
    每当执行一个事务就会产生这样的一条或者多条物理日志。

    为什么需要redolog:
    1. 实现事务的持久性, 让mysql有了崩溃恢复的能力；
    2. 顺序写，比直接写数据到磁盘（随机写）效率更高；

    redolog buffer：
    redolog 也不是每次都会刷盘:
    1. mysql正常关闭时
    2. redolog buffer 达到一半时
    3. 后台线程，每隔1s
    4. 每次事务提交时

    数据安全性和写入性能是熊掌不可得兼的，要不追求数据安全性，牺牲性能；要不追求性能，牺牲数据安全性。
    innodb_flush_log_at_trx_commit
    0： 表示每次事务提交时 ，还是将 redo log 留在 redo log buffer 中 
    1： 都将缓存在 redo log buffer 里的 redo log 直接持久化到磁盘
    2： 写到操作系统的 page cache;

    redo log 采用循环写的方式； 两个指针；
    redo log ib_logfile0 ib_logfile1 磁盘文件（2G） 
    满了会导致mysql不能执行新的更新操作，造成堵塞； 需要停下来,将 Buffer Pool 中的脏页刷新到磁盘中，
    然后标记 redo log 哪些记录可以被擦除，接着对旧的 redo log 记录进行擦除，等擦除完旧记录腾出了空间.

----

### 4. binlog

    redolog 和 undolog 是由 Innodb引擎生成的日志

    binlog是Server层创建的日志
    
##### redolog 和 binlog 的区别

    1. 实现对象不同， redolog是innodb存储引擎实现的日志， binlog是Server层实现的日志

    2. 文件格式不同， binlog 具有 3种格式类型， STATEMENT（记录命令，逻辑日志）， ROW（记录数据）， MIXED
        redolog 是物理日志， 记录某个数据页做了什么修改： 对 XXX 表空间中的 YYY 数据页 ZZZ 偏移量的地方做了AAA 更新；

    3. 写入方式不同， binlog是追加写， redo log 是循环写

    4. 用途不同， binlog 用于备份恢复，主从复制； redolog用于保存buffer pool中的脏页改动，用于掉电等故障恢复；

##### 数据库数据被删除，能用redolog文件恢复数据吗
    不能，得用 binlog文件恢复数据

##### 主从复制

    1. 主库  写入binlog    logdump线程发送binlog日志
    2. 从库io线程  接收binlog日志， 写入 relay log， 返回响应
    3. 从库sql线程， 读取relay log，回放，更新存储引擎中的数据

##### 从库是不是越多越好
    不是， 主从复制需要消耗资源

##### mysql主从复制模型
    1. 同步复制， MySQL 主库提交事务的线程要等待所有从库的复制成功响应； 基本无法使用，性能差，可用性差；
    2. 异步复制（默认 ）， MySQL 主库提交事务的线程并不会等待 binlog 同步到各从库，就返回客户端结果。
        这种模式一旦主库宕机，数据就会发生丢失。
    3. 半同步复制， 半同步复制的方式，兼顾了异步复制和同步复制的优点，
        即使出现主库宕机，至少还有一个从库有最新的数据，不存在数据丢失的风险。

##### binlog什么时候刷盘
    事务执行过程中，先把日志写到 binlog cache（Server 层的 cache），事务提交的时候，再把 binlog cache 写到 binlog 文件中。

---

### 更新语句的执行顺序

    1. 开启事务， 先记录undolog , 更新到buffer pool的Undo 页面；
    2. 执行SQL， 更新数据（更新 buffer pool里的数据页，标记为脏页）
    3. 记录 redo log; (redolog buffer, redolog磁盘日志) 
    
    4. 写 binlog cache
    5. 事务提交时， 将所有binlog刷盘

### 两阶段提交

    事务提交后， redolog 和binlog都要持久化到磁盘；两个独立的逻辑，如果出现半成功的状态，就会导致主从不一致；
    主要是，binlog决定从库数据，redolog决定主库数据；

    MySQL 为了避免出现两份日志之间的逻辑不一致的问题，使用了「两阶段提交」来解决；
    两阶段提交把单个事务的提交拆分成了 2 个阶段，分别是「准备（Prepare）阶段」和「提交（Commit）阶段」

    将 redo log 的写入拆成了两个步骤：prepare 和 commit，中间再穿插写入binlog；

### 两阶段提交的问题

    1. 磁盘 I/O 次数高； 每个事务提交，都会有 redolog 和 binlog 的fsync刷盘；
    2. 锁竞争激烈： 多事务下，为了保证两个日志的提交顺序一致，需要加一个锁；

### 组提交

    
