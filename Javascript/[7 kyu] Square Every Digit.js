// see https://www.codewars.com/kata/546e2562b03326a88e000020
function squareDigits(num){
   let digits = num.toString().split("").map((digit) => digit*digit).join("");
   return +digits
}
