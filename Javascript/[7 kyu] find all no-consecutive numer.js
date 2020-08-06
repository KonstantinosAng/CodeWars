// see https://www.codewars.com/kata/58f8b35fda19c0c79400020f

function allNonConsecutive (arr) {
  if (arr.length === 1) { return [];}
  let rv = []; 
  for (j=0;j<arr.length-1;j++) {
   if (arr[j+1] - arr[j] != 1) {
    rv.push({i: j+1, n: arr[j+1]});
   }
 }
 return rv
}

console.log(allNonConsecutive([1,2,3,4,6,7,8,10]), [{i: 4, n:6}, {i: 7, n:10}])
console.log(allNonConsecutive([-5,-3,-2,0,1,2,3,4,6,7,8,10 ]), [{ i: 1, n: -3 }, { i: 3, n: 0 }, { i: 8, n: 6 }, { i: 11, n: 10 }])