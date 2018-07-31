console.log('hello world');


// 2)
let fname = 'ross';
let lname = 'elpharin';

console.log(`${fname} ${lname}`);

// 3)

let x = 233;
let y = 4;

if(y){
  y = x;
  console.log(y)
}
if(x){
  x = y;
  console.log(x)
}

let x1 = 3.2222;
let y1 = 56.67788;

if(x1 <=y1){
  console.log(y1)
}

let num = -32;

if(num <=50 && num >= -50){
  console.log(true)
}

//# 7 = 15

for (let i =1; i <= 100; i++){
  console.log(i)
}

// #9
for ( let i = 1 ;i <= 100; i++){
  if(i != 17 && i != 43 && i != 100){
    console.log(i)
  }
}
// #10
for(let i = 99; i>= 1; i--){

  if(i /2 % 1){
    console.log(i)
  }
}
