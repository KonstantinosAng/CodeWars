# see https://www.codewars.com/kata/5e8dd197c122f6001a8637ca/train/python

def remove_duplicate_ids(obj):
  store_keys = []
  appeared = []
  for key, value in obj.items():
    store_keys.append(int(key))
  store_keys = [x for x in reversed([x for x in sorted(store_keys)])]
  for i in range(len(store_keys)):
    j = 0
    while j < len(obj[str(store_keys[i])]):
      element = obj[str(store_keys[i])][j]
      if element not in appeared:
        appeared.append(element)
        j += 1
      else:
        obj[str(store_keys[i])].pop(j)
  return obj


from TestFunction import Test

Test = Test(None)
a = {
    "1": ["A", "B", "C"],
    "2": ["A", "B", "D", "A"],
}
res_a = {
    "1": ["C"],
    "2": ["A", "B", "D"]
}
Test.assert_equals(remove_duplicate_ids(a), res_a)

b = {
    "1": ["C", "F", "G"],
    "2": ["A", "B", "C"],
    "3": ["A", "B", "D"],
}
res_b = {
    "1": ["F", "G"],
    "2": ["C"],
    "3": ["A", "B", "D"]
}
Test.assert_equals(remove_duplicate_ids(b), res_b)

c = {
    "1": ["A"],
    "2": ["A"],
    "3": ["A"],
}
res_c = {
    "1": [],
    "2": [],
    "3": ["A"]
}
Test.assert_equals(remove_duplicate_ids(c), res_c)

d = {
    "432": ["A", "A", "B", "D"],
    "53": ["L", "G", "B", "C"],
    "236": ["L", "A", "X", "G", "H", "X"],
    "11": ["P", "R", "S", "D"],
}
res_d = {
    "11": ["P", "R", "S"],
    "53": ["C"],
    "236": ["L", "X", "G", "H"],
    "432": ["A", "B", "D"]
}
Test.assert_equals(remove_duplicate_ids(d), res_d)
