var f1 = function (s) {
    if (typeof s === "string") {
        return s.length;
    }
    return s;
};
console.log(f1('123'));
console.log(f1(123));
console.log(f1([]));
