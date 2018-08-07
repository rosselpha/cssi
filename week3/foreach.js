let txt = '';

let a = [1,2,3,4,5];

let b = [];

function test1 (value, index, array) {
  txt = txt+value+'';
}
function test2 (value, index, array) {
  txt = txt + index + '';
}

function test3 (value, index, array) {
  if(index + 1 <= array.length) {
    b.push(value + array[index + 1]);
  }
}
a.forEach(test1);

console.log(txt);
// 1 2 3 4 5

txt =  "";

a.forEach(test2);

console.log(txt);

//0 1 3 4

a.forEach(test3);

console.log(b)
