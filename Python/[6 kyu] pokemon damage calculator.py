# see https://www.codewars.com/kata/536e9a7973130a06eb000e9f/solutions/python

from TestFunction import Test

def calculate_damage(your_type, opponent_type, attack, defense):
  if your_type == 'fire':
    if opponent_type == 'grass': eff = 2
    elif opponent_type == 'water': eff = 0.5
    elif opponent_type == 'fire': eff = .5
    else: eff = 1
  elif your_type == 'water':
    if opponent_type == 'grass': eff = 0.5
    elif opponent_type == 'water': eff = .5
    elif opponent_type == 'fire': eff = 2
    else: eff = 0.5
  elif your_type == 'grass':
    if opponent_type == 'grass': eff = .5
    elif opponent_type == 'water': eff = 2
    elif opponent_type == 'fire': eff = 0.5
    else: eff = 1
  else:
    if opponent_type == 'grass': eff = 1
    elif opponent_type == 'water': eff = 2
    elif opponent_type == 'fire': eff = 1
    else: eff = .5
  return 50 * (attack / defense) * eff

Test = Test(None)
Test.assert_equals(calculate_damage("fire", "water", 100, 100), 25)
Test.assert_equals(calculate_damage("grass", "water", 100, 100), 100)
Test.assert_equals(calculate_damage("electric", "fire", 100, 100), 50)
Test.assert_equals(calculate_damage("grass", "electric", 57, 19), 150)
Test.assert_equals(calculate_damage("grass", "water", 40, 40), 100)
Test.assert_equals(calculate_damage("grass", "fire", 35, 5), 175)
Test.assert_equals(calculate_damage("fire", "electric", 10, 2), 250)
Test.assert_equals(calculate_damage("grass", "grass", 93, 31), 75)
