# see https://www.codewars.com/kata/5e9df3a0a758c80033cefca1/solutions/python

from TestFunction import Test

def is_int(character):
  try: 
    int(character)
    return True
  except ValueError:
    return False

def no_order(equation):
  found = False
  for value in ['+', '-', '*', '/', '^', '%']:
    if value in equation:
      found = True
  if not found: return int(equation)
  equation = equation.replace(" ", "")
  i = 0
  numbers = []
  operations = []
  i, j = 0, 1
  while i + j <= len(equation):
    if i == len(equation) - 1:
      if is_int(equation[-1]):
        numbers.append(int(equation[-1]))
    if is_int(equation[i:i+j]):
      j += 1
      if i + j == len(equation):
        numbers.append(int(equation[i:]))
        break
    else:
      numbers.append(int(equation[i:i+j-1]))
      i += j
      j = 1
  i = 0
  while i < len(equation):
    if equation[i] in ['+', '-', '*', '/', '^', '%']:
        operations.append(equation[i])
    i += 1
  eq = []
  for v1, v2 in zip(numbers, operations):
    eq.append(v1)
    eq.append(v2)
  eq.append(numbers[-1])
  while len(eq) != 1:
    try:
      if eq[1] == '+':
        value = eq[0] + eq[2]
      elif eq[1] == '-':
        value = eq[0] - eq[2]
      elif eq[1] == '*':
        value = eq[0] * eq[2]
      elif eq[1] == '/':
        value = eq[0] // eq[2]
      elif eq[1] == '^':
        value = eq[0] ** eq[2]
      else:
        value = eq[0]%eq[2]
      eq[0] = value
      eq.pop(1)
      eq.pop(1)
    except:
      return None 
  return value


Test = Test(None)
Test.assert_equals(no_order("2 + 3- 4*1   ^  3"), 1)
Test.assert_equals(no_order("7 *  3 - 3/  10  0"), 0)
Test.assert_equals(no_order("1 20% 0 + 9"), None)
Test.assert_equals(no_order("6 9* 2+6 /  0"), None)
Test.assert_equals(no_order("17/ 7*9  "), 18)
Test.assert_equals(no_order("17+19 % 14*14"), 112)
Test.assert_equals(no_order("17+19 % 14*14"), 112)
Test.assert_equals(no_order("6"), 6)
Test.assert_equals(no_order("20"), 20)
Test.assert_equals(no_order("19^20 - 1+12"), 37589973457545958193355612)
