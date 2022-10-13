// 基础类型

// Boolean
let isDone: boolean = false;
console.log(isDone)

// Number
let decLiteral: number = 6;
let hexLiteral: number = 0xf00d;
let binaryLiteral: number = 0b1010;
let octalLiteral: number = 0o744;
// @ts-ignore
let bigLiteral: bigint = 100n;
console.log(bigLiteral);
console.log(typeof bigLiteral);

// String
let bobname: string = "bob";
let smithname: string = "smith";
let twoname: string = `${bobname} and ${smithname}`
console.log(twoname);


// Array
let list1: number[] = [1, 2, 3];
let list2: Array<number> = [1, 2, 3];


// Tuple
let x: [string, number] = [bobname, decLiteral]
x = ['dafa', 123]
console.log(x)
