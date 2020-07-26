# see https://www.codewars.com/kata/59e19a747905df23cb000024/solutions/python

from TestFunction import Test

def string_letter_count(s):
  counts = {}
  letters = 'abcdefghijklmnopqrstuvwxyz'
  for letter in s:
    if letter.lower() in letters:
      if letter.lower() not in counts:
        counts[letter.lower()] = 1
      else:
        counts[letter.lower()] += 1
  counts = {key: value for key, value in sorted(counts.items(), key=lambda item: item[0])}
  return ''.join(str(value)+str(key) for key, value in counts.items())

Test = Test(None)
Test.assert_equals(string_letter_count("The quick brown fox jumps over the lazy dog."), "1a1b1c1d3e1f1g2h1i1j1k1l1m1n4o1p1q2r1s2t2u1v1w1x1y1z")
Test.assert_equals(string_letter_count("The time you enjoy wasting is not wasted time."), "2a1d5e1g1h4i1j2m3n3o3s6t1u2w2y")
Test.assert_equals(string_letter_count("./4592#{}()"), "")
