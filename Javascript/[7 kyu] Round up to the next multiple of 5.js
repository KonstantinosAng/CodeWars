// see https://www.codewars.com/kata/55d1d6d5955ec6365400006d/solutions/javascript

function roundToNext5(n){
  if (n === 0) { return 0; }
  if (n === -5) { return -5; }
  if (n > 0) {
    if (Math.floor(n%5) === 0 & n >= 5) { 
      return n;
    }
    else { 
      return (Math.floor(n/5) + 1)*5;
    }
  } else {
    if (Math.floor(n%5) === 0 & n >= -5) { 
      return n;
    }
    else { 
      if (Math.floor(n%5) === 0) { return n }
      else { return (Math.floor(n/5) + 1)*5; }
    }
  }
}


[[0,0],
 [1,5],
 [3,5],
 [5,5],
 [7,10],
 [39,40]].forEach(([x,out])=> console.log(roundToNext5(x) === out ));
