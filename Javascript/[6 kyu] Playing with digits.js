//see https://www.codewars.com/kata/5552101f47fc5178b1000050/solutions/javascript

function digPow(n, p){
  let sum = 0;
  let number = 0;
  let digits = n.toString().split("").map((digit) => {
    sum += +Math.pow(digit, p+number);
    number++;
  });
  if (sum%n === 0) {
    return sum/n
  } else {
    return -1
}