//see https://www.codewars.com/kata/525c65e51bf619685c000059/solutions/javascript

function cakes(recipe, available) {
  var min = -1;
  var cakes = 0;
  var found = false;
  for (var key in available) {
    if (recipe[key]) {
      found = true;
      cakes = Math.floor(available[key]/recipe[key]);
      if (min === -1) {
        min = cakes;
      }
      if (cakes < min) {
        min = cakes;
      }
    }
  }
  for (var key in recipe) {
    if (!available[key]) { found = false }
  }
  if (!found) { return 0}
  return min
}