// 基础类型
// Boolean
var isDone = false;
console.log(isDone);
// Number
var decLiteral = 6;
var hexLiteral = 0xf00d;
var binaryLiteral = 10;
var octalLiteral = 484;
// @ts-ignore
var bigLiteral = 100n;
console.log(bigLiteral);
console.log(typeof bigLiteral);
// String
var bobname = "bob";
var smithname = "smith";
var twoname = "".concat(bobname, " and ").concat(smithname);
console.log(twoname);
// Array
var list1 = [1, 2, 3];
var list2 = [1, 2, 3];
// Tuple
var x = [bobname, decLiteral];
x = ['dafa', 123];
console.log(x);
