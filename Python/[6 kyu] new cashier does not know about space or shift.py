# see https://www.codewars.com/kata/5d23d89906f92a00267bb83d/solutions/python

from TestFunction import Test

def get_order(order):
  orders = {'burger': 0, 'fries': 0, 'chicken': 0, 'pizza': 0, 'sandwich': 0, 'onionrings': 0, 'milkshake': 0, 'coke': 0}
  ret = ''
  for key, value in orders.items():
    orders[key] = order.count(f'{key}')
    rv = ' '.join(key.capitalize() for i in range(order.count(key)))
    if orders[key] == 0:
      ret += ''
    else:
      ret += rv + ' '
  return ret[:-1]


Test = Test(None)
Test.assert_equals(get_order("milkshakepizzachickenfriescokeburgerpizzasandwichmilkshakepizza"),
                    "Burger Fries Chicken Pizza Pizza Pizza Sandwich Milkshake Milkshake Coke")
Test.assert_equals(get_order("pizzachickenfriesburgercokemilkshakefriessandwich"),
                    "Burger Fries Fries Chicken Pizza Sandwich Milkshake Coke")
