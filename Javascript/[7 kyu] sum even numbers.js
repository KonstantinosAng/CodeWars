// see https://www.codewars.com/kata/586beb5ba44cfc44ed0006c3/train/javascript

function sumEvenNumbers(input) {
  let sum = 0;
  input.forEach((value) => {
    if (value%2 === 0 && value%1 === 0) {
      sum += value;
    }
  });
  return sum
}

console.log(sumEvenNumbers([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]), 30);
