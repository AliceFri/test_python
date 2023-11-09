var tom = ['a', 12];
tom[0] = 'a';
tom[0] = 'b';
console.log(tom);
tom[1] = 25;
// 越界时报错
tom.push(1, 2, 3);
console.log(tom);
