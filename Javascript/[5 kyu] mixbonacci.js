// see https://www.codewars.com/kata/5811aef3acdf4dab5e000251/train/javascript

var fib_memo = {};

function fib(n) {
  if (n in fib_memo) {
    value = fib_memo[n];
  } else {
    if (n === 1) { value = 0; }
    else if (n === 2) { value = 1; }
    else { 
      value = fib(n-1) + fib(n-2);
      fib_memo[n] = value;
    }
  }
  return value
}

var tri_memo = {};

function tri(n) {
  if (n in tri_memo) {
    value = tri_memo[n];
  } else {
    if (n <= 2) { value = 0; }
    else if (n === 3) { value = 1; }
    else { 
      value = tri(n-1) + tri(n-2) + tri(n-3);
      tri_memo[n] = value;
    }
  }
  return value;
}

var tet_memo = {};

function tet(n) {
  if (n in tet_memo) {
    value = tet_memo[n];
  } else {
    if (n <= 3) { value = 0; }
    else if (n === 4) { value = 1; }
    else {
      value = tet(n-1) + tet(n-2) + tet(n-3) + tet(n-4);
      tet_memo[n] = value;
    }
  }
  return value;
}

function pad(n) {
    if (n === 1) { return 1; }
    if (n <= 3) { return 0; }
    else { 
      return pad(n-2) + pad(n-3);
    }
}

var jac_memo = {};

function jac(n) {
  if (n in jac_memo) { value = jac_memo[n]; }
  else {
    if (n === 1) { value = 0; }
    else if (n === 2) { value = 1; }
    else {
      value = jac(n-1) + 2*jac(n-2);
      jac_memo[n] = value;
    }
  }
  return value;
}

var pel_memo = {};

function pel(n) {
  if (n in pel_memo) { value = pel_memo[n]; }
  else {
    if (n === 1) { value = 0; }
    else if (n === 2) { value = 1; }
    else { 
    value = 2*pel(n-1) + pel(n-2);
    pel_memo[n] = value;
   }
  }
  return value;
}

function mixbonacci(pattern, length) {
  if (pattern.length === 0) { return []; }
  if (length === 0) { return []; }
  let rv = [];
  let count = {'fib': 1, 'pad': 1, 'jac': 1, 'pel': 1, 'tri': 1, 'tet': 1};
  while (rv.length<length) {
    for (let j=0;j<pattern.length;j++) {
      if (pattern[j] === 'fib') {
        rv.push(fib(count[pattern[j]]));
      } else if (pattern[j] === 'pad') {
        rv.push(pad(count[pattern[j]]));
      } else if (pattern[j] === 'jac') {
        rv.push(jac(count[pattern[j]]));
      } else if (pattern[j] === 'pel') {
        rv.push(pel(count[pattern[j]]));
      } else if (pattern[j] === 'tri') {
        rv.push(tri(count[pattern[j]]));
      } else {
        rv.push(tet(count[pattern[j]]));
      }
      count[pattern[j]] += 1;
      if (rv.length == length) { break; }
    }
  }
  return rv;
}

var tests = [
  [[[], 10], []],
  [[['fib'], 0], []],
  [[['fib'], 10], [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]],
  [[['pad'], 10], [1, 0, 0, 1, 0, 1, 1, 1, 2, 2]],
  [[['jac'], 10], [0, 1, 1, 3, 5, 11, 21, 43, 85, 171]],
  [[['pel'], 10], [0, 1, 2, 5, 12, 29, 70, 169, 408, 985]],
  [[['tri'], 10], [0, 0, 1, 1, 2, 4, 7, 13, 24, 44]],
  [[['tet'], 10], [0, 0, 0, 1, 1, 2, 4, 8, 15, 29]],
  [[['fib', 'tet'], 10], [0, 0, 1, 0, 1, 0, 2, 1, 3, 1]],
  [[['jac', 'jac', 'pel'], 10], [0, 1, 0, 1, 3, 1, 5, 11, 2, 21]],
  [[[ 'tri', 'fib', 'pad', 'fib', 'fib', 'tri', 'pad', 'tri', 'tri', 'pad' ], 26], [0, 0, 1, 1, 1, 0, 0, 1, 1, 0, 2, 2, 1, 3, 5, 4, 0, 7, 13, 1, 24, 8, 1, 13, 21, 44]],
  [[[ 'pel', 'tri' ], 54], [0, 0, 1, 0, 2, 1, 5, 1, 12, 2, 29, 4, 70, 7, 169, 13, 408, 24, 985, 44, 2378, 81, 5741, 149, 13860, 274, 33461, 504, 80782, 927, 195025, 1705, 470832, 3136, 1136689, 5768, 2744210, 10609, 6625109, 19513, 15994428, 35890, 38613965, 66012, 93222358, 121415, 225058681, 223317, 543339720, 410744, 1311738121, 755476, 3166815962, 1389537]],
]

for (var i = 0, l = tests.length; i < l; i++) {
  var tst = tests[i];
  var inp = tst[0];
  var exp = tst[1];
  var pattern = inp[0];
  var length = inp[1];
  console.log(mixbonacci(pattern, length));
}  
