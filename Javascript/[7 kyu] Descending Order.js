// see https://www.codewars.com/kata/5467e4d82edf8bbf40000155

function descendingOrder(n){
   var digits = (""+n).split("").sort((a,b) => b-a).join("");
   return +digits
}
