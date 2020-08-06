// see https://www.codewars.com/kata/5a8d1c82373c2e099d0000ac/solutions/javascript

function solve(st,a,b){
  let rev = [];
  for (let i=0;i<=st.length;i++) {
    if (i >= a && i <= b) {
      rev.push(st[i]);
    }
  }    
  rev = rev.reverse().join("");
  let rv = '';
  let i = 0;
  st.split("").forEach((value, index) => {
    if (index >= a && index <= b) {
      rv += rev[i];
      i++;
    } else {
      rv += value;
    }
  });
  return rv
}


console.log(solve("codewars",1,5),"cawedors");
console.log(solve("codingIsFun",2,100),"conuFsIgnid");
console.log(solve("FunctionalProgramming", 2,15),"FuargorPlanoitcnmming");
console.log(solve("abcdefghijklmnopqrstuvwxyz",0,20),"utsrqponmlkjihgfedcbavwxyz");
console.log(solve("abcdefghijklmnopqrstuvwxyz",5,20),"abcdeutsrqponmlkjihgfvwxyz");
