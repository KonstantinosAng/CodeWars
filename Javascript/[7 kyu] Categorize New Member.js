// see https://www.codewars.com/kata/5502c9e7b3216ec63c0001aa/solutions/javascript

function openOrSenior(data){
   let arr = [];
   data.map(value => {
    if (value[0] >= 55 & value[1] > 7) {
       arr.push("Senior");
    } else {
       arr.push("Open");
    }
   })
   return arr
}
