// see https://www.codewars.com/kata/5ac54bcbb925d9b437000001/solutions/javascript

function findMiddle(str) {
  if (str === null) { return -1; }
  if (typeof str !== 'string') { return -1; }
  let mul = 1;
  let found = false;
  str = str.replace(/\s/g, '');
  if (str === '') { return -1; }
  str.split('').forEach((value) => {
    if (!isNaN(value)) {
      mul *= value;
      found = true;
    }
  });
  if (!found) { return -1; }
  mul = mul.toString();
  if (mul.length%2 === 0) { 
    return +(mul[mul.length/2-1]+mul[mul.length/2]);
  } else {
    return +mul[Math.floor(mul.length/2)];
  }
}

//console.log(findMiddle('s7d8jd9'), 0);
//console.log(findMiddle('58jd9fgh/fgh6s.,sdf'), 16);
//console.log(findMiddle([ 1, 2, 3, 4, 5, 6 ]), 2);
//console.log(findMiddle('         '), -1);
console.log(findMiddle('asd.fasd.gasdfgsdf1gh-sdfghsdfg/asdfga=sdfg'), 1);