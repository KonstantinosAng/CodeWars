# see https://www.codewars.com/kata/5b180e9fedaa564a7000009a/solutions/python

def solve(s):
  upper = sum(1 for character in s if character.isupper())
  if upper > len(s) - upper: 
    return s.upper()  
  else: 
    return s.lower()

print(solve("code") == "code")
print(solve("CODe") == "CODE")
print(solve("COde") == "code")
print(solve("Code") == "code")