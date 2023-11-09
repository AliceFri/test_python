http://www.patrickzhong.com/TypeScript/zh/reference/iterators-and-generators.html

https://ts.xcatliu.com/introduction/what-is-typescript.html


类型：
    boolean             布尔值
    number              数值
    string              字符串
    void                空值
    null/undefined      所有类型的子类型
    
    any                 任意类型 （变量如果在声明的时候，未指定其类型，那么它会被识别为任意值类型）

联合类型：
    string | numbser    字符串或数值类型

接口类型：
    关键字 interface;支持可选， 任意， readonly
interface IPerson {
    readonly id: number;
    name: string;
    age?: number;
    [propName: string]: any;
}

类型断言:
class ApiError extends Error {
    code: number = 0;
}
class HttpError extends Error {
    statusCode: number = 200;
}

function isApiError(error: Error) {
    if (typeof (error as ApiError).code === 'number') {
        return true;
    }
    return false;
}
双重断言：
function testCat(cat: Cat) {
    return (cat as any as Fish);
}


进阶：
1. 类型别名, 常用于 联合类型
   type Name = string;
   type NameResolver = () => string;
   type NameOrResolver = Name | NameResolver;

2. 字符串字面量类型
   字符串字面量类型用来约束取值只能是某几个字符串中的一个。
   type EventNames = 'click' | 'scroll' | 'mousemove';

3. 元组
