// see https://www.codewars.com/kata/5eea52f43ed68e00016701f3/train/javascript

// function fib (n) {
//   if (n == 1) { return 0; }
//   if (n == 2) { return 1; }  
//   return fib(n-2) + fib(n-1);
// }

// function countWays(n, k){
//   return fib(k+n)-1;
// }

function countWays(n, k){
  let li = new Array(k).fill(null).map((_, y)=>2**y)
  for (let _=0;_<n-k;_++) li.push(li.slice(-k).reduce((x,y)=>x+y))
  return li[n-1]
}

console.log(countWays(1, 3), 1);
console.log(countWays(3, 3), 4);
console.log(countWays(2, 3), 2);
console.log(countWays(5, 3), 13);
console.log(countWays(4, 3), 7);
console.log(countWays(10, 6), 492);
console.log(countWays(14, 7), 7936);
