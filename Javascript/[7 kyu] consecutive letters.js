// see https://www.codewars.com/kata/5ce6728c939bf80029988b57/solutions/javascript

function solve(s){
  s = s.split('').sort();
  for (let i=0;i<s.length-1;i++) {
    if (s[i+1].charCodeAt(0) - s[i].charCodeAt(0) != 1) {
      return false
    }
  };
  return true
}


console.log(solve("abc"),true);
console.log(solve("abd"),false);
console.log(solve("dabc"),true);
console.log(solve("abbc"),false);
