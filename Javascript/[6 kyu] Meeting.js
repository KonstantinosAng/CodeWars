//see https://www.codewars.com/kata/59df2f8f08c6cec835000012/solutions/javascript

function meeting(s) {
  var ret = [];
  var string = "";
  s.split(";").map((str) => {
    var name = str.split(":");
    ret.push([name[1].toUpperCase(), name[0].toUpperCase()]);
  });
  ret.sort().map((name) => {
    string += `(${name[0]}, ${name[1]})`;
  });
  return string
}