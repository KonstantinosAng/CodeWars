# see https://www.codewars.com/kata/54bf1c2cd5b56cc47f0007a1/solutions/python

from TestFunction import Test

def duplicate_count(text):
  counts = {}
  for t in text:
    if t.lower() not in counts:
      counts[t.lower()] = 1
    else:
      counts[t.lower()] += 1
  return sum([1 for key, value in counts.items() if value > 1])
     

Test = Test(None)
Test.assert_equals(duplicate_count("abcde"), 0)
Test.assert_equals(duplicate_count("abcdea"), 1)
Test.assert_equals(duplicate_count("indivisibility"), 1)
