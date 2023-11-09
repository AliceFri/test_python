interface Person {
    name: string;
    age: number;
}

// 必须保持一致， 多属性， 少属性都不行
let tom: Person = {
    name: '123',
    age: 12,
    // a: 1
}

// 可选属性
interface IPerson1 {
    name: string;
    age?: number;
}

let k1: IPerson1 = {
    name: 'k1'
}
let k2: IPerson1 = {
    name: 'k2',
    age: 12
}

// 任意属性
interface IPerson2 {
    name: string;
    age?: number;
    [name: string]: any;
}

let a1: IPerson2 = {
    name: 'a1',
    age: 12,
    gender: 'male'
}

// 只读属性
interface IPerson {
    readonly id: number;
    name: string;
    age?: number;
    [propName: string]: any;
}

