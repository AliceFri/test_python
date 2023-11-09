// 函数声明
function sum(x, y) {
    return x + y;
}

function tsSum(x: number, y: number): number {
    return x + y
}

tsSum(1, 2)

// 函数表达式
let mySum = function (x, y) {
    return x + y;
}

let mytsSum: (x: number, y: number) => number = function (x: number, y: number): number {
    return x + y;
};

// 可选参数
function buildName(firstName: string, lastName?: string) {
    return firstName + ' ' + lastName
}

console.log(buildName('tom'))

// 参数默认值
function buildName1(firstName: string, lastName: string = 'cat') {
    return firstName + ' ' + lastName
}
console.log(buildName1('tom'))

// 剩余参数
function push(array: any[], ...items: any[]) {
    console.log(items)
    return array
}

function reverse(x: number): number;
function reverse(x: string): string;
function reverse(x: number | string): number | string | void {
    if (typeof x === 'number') {
        return Number(x.toString().split('').reverse().join(''));
    } else if (typeof x === 'string') {
        return x.split('').reverse().join('');
    }
}

