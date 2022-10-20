// [类型 + 方括号] 表示法
let fibonacci: number[] = [1, 1, 2, 3, 5]

// 数组 泛型
let a1: Array<number> = [1, 2, 3, 4, 5]

// 接口表示数组
interface NumberArray {
    [i: number]: number;
}
let a2: NumberArray = {
    1: 1,
    2: 2,
    '-3': -3
}
let a3: NumberArray = [0, 1]

// 类数组
function sum1() {
    let args1: {
        [i: number]: number;
        length: number;
        callee: Function;
    } = arguments
}

function sum() {
    let args: IArguments = arguments
}

// Any 在数组中的应用
let list: any[] = [1, 'a', {}]