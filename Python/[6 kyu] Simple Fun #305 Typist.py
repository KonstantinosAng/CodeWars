# see https://www.codewars.com/kata/5544c7a5cb454edb3c000047/train/python

def typist(s):
  caps, count = False, 0
  for letter in s:
    if letter.lower() == letter:
      if caps: 
        caps = False
        count += 1
      count += 1
    else:
      if not caps:
        caps = True
        count += 1
      count += 1
  return count


from TestFunction import Test
test = Test(None)

sample_test_cases = [
    ('Basic tests', [
        ('a', 1),
        ('aa', 2),
        ('A', 2),
        ('AA', 3),
        ('aA', 3),
        ('Aa', 4),
    ]),
    ('Longer words', [
        ('BeiJingDaXueDongMen', 31),
        ('AAAaaaBBBbbbABAB', 21),
        ('AmericanRAILWAY', 18),
        ('AaAaAa', 12),
        ('DFjfkdaB', 11),
    ]),
]

test.describe('Sample tests')
for name, test_cases in sample_test_cases:
  test.it(name)
  for s, expected in test_cases:
    test.assert_equals(typist(s), expected)
