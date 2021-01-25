# see https://www.codewars.com/kata/59c3e819d751df54e9000098/train/python

from TestFunction import Test

def loose_change(cents):
  change_dict = {'Nickels': 0, 'Pennies': 0, 'Dimes': 0, 'Quarters': 0}
  if cents <= 0: return change_dict
  while cents >= 1:
    if cents >= 25:
      change_dict['Quarters'] += 1
      cents -= 25
    elif cents >= 10:
      change_dict['Dimes'] += 1
      cents -= 10
    elif cents >= 5:
      change_dict['Nickels'] += 1
      cents -= 5
    else:
      change_dict['Pennies'] += 1
      cents -= 1
  return change_dict


test = Test(None)
test.assert_equals(loose_change(29),  {'Nickels': 0, 'Pennies': 4, 'Dimes': 0, 'Quarters': 1})
test.assert_equals(loose_change(91),  {'Nickels': 1, 'Pennies': 1, 'Dimes': 1, 'Quarters': 3})
test.assert_equals(loose_change(0),   {'Nickels': 0, 'Pennies': 0, 'Dimes': 0, 'Quarters': 0})
test.assert_equals(loose_change(-2),  {'Nickels': 0, 'Pennies': 0, 'Dimes': 0, 'Quarters': 0})
test.assert_equals(loose_change(3.9), {'Nickels': 0, 'Pennies': 3, 'Dimes': 0, 'Quarters': 0})