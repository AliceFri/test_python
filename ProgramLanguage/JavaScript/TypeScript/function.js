// 函数声明
function sum(x, y) {
    return x + y;
}
function tsSum(x, y) {
    return x + y;
}
tsSum(1, 2);
// 函数表达式
var mySum = function (x, y) {
    return x + y;
};
var mytsSum = function (x, y) {
    return x + y;
};
// 可选参数
function buildName(firstName, lastName) {
    return firstName + ' ' + lastName;
}
console.log(buildName('tom'));
// 参数默认值
function buildName1(firstName, lastName) {
    if (lastName === void 0) { lastName = 'cat'; }
    return firstName + ' ' + lastName;
}
console.log(buildName1('tom'));
// 剩余参数
function push(array) {
    var items = [];
    for (var _i = 1; _i < arguments.length; _i++) {
        items[_i - 1] = arguments[_i];
    }
    console.log(items);
    return array;
}
function reverse(x) {
    if (typeof x === 'number') {
        return Number(x.toString().split('').reverse().join(''));
    }
    else if (typeof x === 'string') {
        return x.split('').reverse().join('');
    }
}
