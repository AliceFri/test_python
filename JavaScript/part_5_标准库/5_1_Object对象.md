### 1. 概述

JavaScript 原生提供 Object 对象
所有其他对象都 继承自 Object 对象

Object 对象的原生方法 分为两类： 本身的方法， 实例方法

#### 1.1 Object 本身的方法

    直接定义在 Object 对象的 方法

    Object.print = function (o) { console.log(o) };

#### 1.2 Object 的实例方法
    
    定义在 Object 原型对象 Object.prototype 上的方法

----------------------

### 2. Object()

Object 本身是一个函数， 可以将任何值转为对象

----------------------

### 3. Object 构造函数

var obj = new Object();

----------------------

### 4. Object 的静态方法（对象自身的方法）

Object.keys 方法和 Object.getOwnPropertyNames 方法都用来遍历对象的属性

    Object.getOwnPropertyDescriptor()：获取某个属性的描述对象。
    Object.defineProperty()：通过描述对象，定义某个属性。
    Object.defineProperties()：通过描述对象，定义多个属性。

    Object.preventExtensions()：防止对象扩展。
    Object.isExtensible()：判断对象是否可扩展。
    Object.seal()：禁止对象配置。
    Object.isSealed()：判断一个对象是否可配置。
    Object.freeze()：冻结一个对象。
    Object.isFrozen()：判断一个对象是否被冻结。

    Object.create()：该方法可以指定原型对象和属性，返回一个新的对象。
    Object.getPrototypeOf()：获取对象的Prototype对象。

--------------------------

### 5. Object 的实例方法

    Object.prototype.valueOf()：返回当前对象对应的值。
    Object.prototype.toString()：返回当前对象对应的字符串形式。
    Object.prototype.toLocaleString()：返回当前对象对应的本地字符串形式。
    Object.prototype.hasOwnProperty()：判断某个属性是否为当前对象自身的属性，还是继承自原型对象的属性。
    Object.prototype.isPrototypeOf()：判断当前对象是否为另一个对象的原型。
    Object.prototype.propertyIsEnumerable()：判断某个属性是否可枚举。
