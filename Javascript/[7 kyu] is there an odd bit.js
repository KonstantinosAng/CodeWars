// see https://www.codewars.com/kata/5d6f49d85e45290016bf4718/solutions

/* function anyOdd(x) {
  x = ('0b' + x.toString(2)).split('');
  console.log(x)
  for (let i=0;i<x.length;i++) {
    if (i%2 !== 0) {
      if (x[i] === '1') { 
        return 1
      }
    }
  }
  return 0
} */

const MATCH = parseInt('10'.repeat(16),2);

function anyOdd(x) {
    return !!(x & MATCH) * 1;
}

console.log(anyOdd(2863311530), 1);
console.log(anyOdd(128), 1);
console.log(anyOdd(131), 1);
console.log(anyOdd(2), 1);
console.log(anyOdd(24082), 1);
console.log(anyOdd(0), 0);
console.log(anyOdd(85), 0);
console.log(anyOdd(1024), 0);
console.log(anyOdd(1), 0);
console.log(anyOdd(1365), 0);
console.log(anyOdd(170), 1);
console.log(anyOdd(5), 0);
