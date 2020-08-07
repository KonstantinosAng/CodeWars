// see https://www.codewars.com/kata/5413759479ba273f8100003d/solutions/javascript

reverse = function(array) {
  let rv = [];
  for (let i=array.length-1;i>=0;i--) {
    rv.push(array[i]);
  }
  return rv;
}

console.log( reverse([1,2,3]), [3,2,1] );
console.log( reverse([1,null,14,"two"]), ["two",14,null,1] );