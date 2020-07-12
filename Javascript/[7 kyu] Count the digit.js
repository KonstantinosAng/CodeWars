// see https://www.codewars.com/kata/566fc12495810954b1000030/solutions/javascript

function nbDig(n, d) {
  let squares = [];  
  for (let i = 0; i <= n; i++) {
     squares.push(i*i);   
  }
  var sum = 0;
  squares.map((square) => {
    if (square.toString().includes(d.toString())) {
      sum += square.toString().split(d.toString()).length - 1;
    }
  })
  return sum
}