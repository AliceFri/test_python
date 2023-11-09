const f1 = (s: string | number) => {
    if (typeof s === "string") {
        return s.length;
    }
    return s
}

console.log(f1('123'))
console.log(f1(123))
// console.log(f1([]))

