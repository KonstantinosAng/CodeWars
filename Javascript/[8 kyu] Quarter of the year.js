// see https://www.codewars.com/kata/5ce9c1000bab0b001134f5af/solutions/javascript

const quarterOf = (month) => {
  if (month <= 3) { return 1 }
  if (month <= 6) { return 2 }
  if (month <= 9) { return 3 }
  if (month <= 12) { return 4 }
}