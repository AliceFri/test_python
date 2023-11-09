### 1. 代码结构

    schema.ts	# 数据库 collections 结构
    controller.ts	# 前端接口层	A basic controller with a single route.
        Controllers are responsible for handling incoming requests and returning responses to the client.
    controller.spec.ts	# The unit tests for the controller.
    dto.ts		# 返回给前端接口的model
    service.ts	# 逻辑层
    module.ts	# The (root) module of the application.
    
    main.ts	# The entry file of the application which uses the core function NestFactory to create a Nest application instance.

-------------------

@Global 是什么
@Module 是什么

### 2. 相关库

#### 2.0 @nestjs/common 库
    装饰器：
    @Controller  装饰一组路由的类，可以给路由加上公共前缀，eg: @Controller('cats')
    @Get @Post @Put @Delete ... 装饰接受路由请求的方法，    
    
    @Injectable     附加元数据，元数据声明 CatsService 是一个可以由 Nest IoC 容器管理的类。成为Provider（生产者）
    @Inject         属性注入

    @Module         provides metadata that Nest makes use of to organize the application structure.
        providers
        controllers
        imports
        exports
    @Global         decorator makes the module global-scoped. Global modules should be registered only once



#### 2.1 @nestjs/mongoose 库
	1. 连接数据库 app.module.ts	文件
	2. Model injection
	
	装饰器:
	@Schema() decorator marks a class as a schema definition. 
	@Prop() decorator defines a property in the document. 
	
	# 批量创建
	await this.users.bulkWrite(
      		users.map(user => ({
        	  updateOne: {
          		filter: {
            			userid: user.userid,
          			},
          		update: user,
          		upsert: true,
        		},
      		})),
    	);

    # 获取
    this.users.find(
    { status },
    { userid: true, name: true },
    ).lean<Pick<User, 'userid' | 'name'>[]>();

--------------------

### 3. Others

ts相关语法:
Promise, Pick:	Promise<Pick<User, 'userid' | 'name'>[]


logger?

@nestjs/config
@nestjs/swagger

    @Req() req: Request,    req.sessions



run-rs --mongod --keep --dbpath ~/trgs/data --portStart 28000
Skipping purge
Running 'mongod' [ 28000, 28001, 28002 ]
Restarting replica set...
Started replica set on "mongodb://localhost:28000,localhost:28001,localhost:28002?replicaSet=rs"
Connected to oplog
(node:2856511) [MONGODB DRIVER] DeprecationWarning: collection.find option [oplogReplay] is deprecated and will be removed in a later version.
(Use `node --trace-deprecation ...` to show where the warning was created)