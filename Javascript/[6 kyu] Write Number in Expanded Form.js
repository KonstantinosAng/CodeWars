// see https://www.codewars.com/kata/5842df8ccbd22792a4000245/solutions/javascript

function zeros (num) {
  if (num === 0) {return ""}
  if (num === 1) {return "0"}
  var s = "";
  for (let i=1;i<=num;i++) {
    s += "0";
  }
  return s
}

function expandedForm(num) {
  var repr = "";
  var decs = num.toString().length-1;
  num.toString().split("").map((digit) => {
    if (digit !== "0") {
      repr += digit + zeros(decs) + " + ";
    }
    decs--; 
  })
  return repr.substring(0, repr.length-3)
}