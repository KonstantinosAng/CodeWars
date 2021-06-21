function streetFighterSelection(fighters, position, moves) {
  let fightersChosen = [];
  if (moves.length === 0) { return fightersChosen }
  for (const move of moves) {
    if (move === 'up') {
      position[1]--;
    } else if (move === 'down') {
      position[1]++;
    } else if (move === 'right') {
      position[0]++;
    } else if (move === 'left') {
      position[0]--;
    }
    if (position[1] >= fighters.length) {
      position[1] = fighters.length - 1;
    }
    if (position[1] < 0) {
      position[1] = 0;
    }
    if (position[0] < 0) {
      position[0] = fighters[0].length + position[0];
    }
    if (position[0] >= fighters[0].length) {
      position[0] -= 6; 
    }
    fightersChosen.push(fighters[position[1]][position[0]])
  }
  return fightersChosen
}

fighters = [
	["Ryu", "E.Honda", "Blanka", "Guile", "Balrog", "Vega"],
	["Ken", "Chun Li", "Zangief", "Dhalsim", "Sagat", "M.Bison"]
];

moves = ['up', 'left', 'right', 'left', 'left'];
console.log(streetFighterSelection(fighters, [0,0], moves), ['Ryu', 'Vega', 'Ryu', 'Vega', 'Balrog'])


moves = ["left","left","left","left","left","left","left","left"];
console.log(streetFighterSelection(fighters, [0,0], moves), ['Vega', 'Balrog', 'Guile', 'Blanka', 'E.Honda', 'Ryu', 'Vega', 'Balrog'])


moves = ["right","right","right","right","right","right","right","right"];
console.log(streetFighterSelection(fighters, [0,0], moves), ['E.Honda', 'Blanka', 'Guile', 'Balrog', 'Vega', 'Ryu', 'E.Honda', 'Blanka']);

moves = ["up","left","down","right","up","left","down","right"];
console.log(streetFighterSelection(fighters, [0,0], moves), ['Ryu', 'Vega', 'M.Bison', 'Ken', 'Ryu', 'Vega', 'M.Bison', 'Ken']);


moves = ["down","down","down","down"];
console.log(streetFighterSelection(fighters, [0,0], moves), ['Ken', 'Ken', 'Ken', 'Ken']);


moves = ["up","up","up","up"];
console.log(streetFighterSelection(fighters, [0,0], moves), ['Ryu', 'Ryu', 'Ryu', 'Ryu']);

moves = [];
console.log(streetFighterSelection(fighters, [0,0], moves), [])