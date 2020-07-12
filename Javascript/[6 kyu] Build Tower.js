// see https://www.codewars.com/kata/576757b1df89ecf5bd00073b/solutions/javascript

function repeatStr(str, num) {
  if (Math.floor(num) === 0) { return '' }
  if (Math.floor(num) === 1) { return str }
  let s = '';
  for (let i = 1; i <= Math.floor(num); i++) {
    s += str;
  }
  return s;
}
  
function towerBuilder(nFloors) {
  const biggestAsterisk = 2*nFloors - 1;
  let arr = [];
  for (let i = 1; i <= nFloors; i++) {
    let floor = "";
    let spaces = repeatStr(" ", (biggestAsterisk - 2*i + 1)/2);
    floor = spaces + repeatStr("*", 2*i - 1) + spaces;  
    arr.push(floor);
  }
  return arr;
}