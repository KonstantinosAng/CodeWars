# see https://www.codewars.com/kata/5616868c81a0f281e500005c/solutions/python

from TestFunction import Test

def rank(st, we, n):
  if st == "": return "No participants"
  if n > len(st.split(",")): return "Not enough participants"
  ranks = {}
  st = st.split(",")
  for name, weight in zip(st, we):
    ranks[name] = (len(name) + sum([ord(letter.lower()) - 96 for letter in name]))*weight
  ranks = {k: v for k, v in sorted(ranks.items(), key=lambda item: item[1])}
  names, ranks = [k for k in ranks], [v for k, v in ranks.items()]
  names = [name for name in reversed(names)]
  ranks = [rank for rank in reversed(ranks)]
  sorted_names, i = [], 0
  while i <= len(names) - 1:
    if i + 1 <= len(names) - 1 and ranks[i] == ranks[i + 1]:
      if ord(names[i][0]) <= ord(names[i + 1][0]):
        sorted_names.append(names[i])
        sorted_names.append(names[i + 1])
      else:
        sorted_names.append(names[i + 1])  
        sorted_names.append(names[i])
      i += 1  
    else:
      sorted_names.append(names[i])
    i += 1
  print(sorted_names)
  return sorted_names[n-1]


Test = Test(None)
Test.assert_equals(rank("Addison,Jayden,Sofia,Michael,Andrew,Lily,Benjamin", [4, 2, 1, 4, 3, 1, 2], 4), "Benjamin")
Test.assert_equals(rank("Lagon,Lily", [1, 5], 2), "Lagon")
Test.assert_equals(rank("Addison,Jayden,Sofia,Michael,Andrew,Lily,Benjamin", [4, 2, 1, 4, 3, 1, 2], 8), "Not enough participants")
Test.assert_equals(rank("", [4, 2, 1, 4, 3, 1, 2], 6), "No participants")
Test.assert_equals(rank("Elijah,Chloe,Elizabeth,Matthew,Natalie,Jayden", [1, 3, 5, 5, 3, 6], 2), "Matthew")
Test.assert_equals(rank("Aubrey,Olivai,Abigail,Chloe,Andrew,Elizabeth", [3, 1, 4, 4, 3, 2], 4), "Abigail")
Test.assert_equals(rank("William,Willaim,Olivia,Olivai,Lily,Lyli", [1, 1, 1, 1, 1, 1], 1), "Willaim")
