// see https://www.codewars.com/kata/5bf774a81505a7413400006a/solutions/javascript

function fix(paragraph){
  if (paragraph === "") { return "" } 
  let ret = "";
  paragraph = paragraph.split(".");
  for (let i=0;i<paragraph.length-1;i++) {
    if (i == 0) {
      ret += paragraph[i].charAt(0).toUpperCase() + paragraph[i].slice(1) + ".";  
    } else {
      ret +=  " " + paragraph[i].charAt(1).toUpperCase() + paragraph[i].slice(2) + ".";
    }
  }
  return ret
}


console.log(fix("") === "")
console.log(fix("hi.") === "Hi.")
console.log(fix("hello. my name is inigo montoya. you killed my father. prepare to die.") ===
  		"Hello. My name is inigo montoya. You killed my father. Prepare to die.")