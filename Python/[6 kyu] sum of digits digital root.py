# see https://www.codewars.com/kata/52dffa05467ee54b93000712/solutions/pythons

from TestFunction import Test

def pseudo_sort(st):
  punctuations = [',', '.', '!', ':', '?', ';']
  for punc in punctuations:
    st = st.replace(punc, "") 
  if st.isspace(): return '' 
  words = st.split(" ")
  lowercase = []
  uppercase = []
  for word in words:
    if word.lower() == word:
      lowercase.append(word)
    else:
      uppercase.append(word)
  lowercase = ' '.join([x for x in sorted(lowercase)])
  uppercase = ' '.join([x for x in reversed(sorted(uppercase))])
  if lowercase == '': return uppercase
  if uppercase == '': return lowercase
  return ' '.join([lowercase, uppercase])

test = Test(None)
test.assert_equals(pseudo_sort("I, habitan of the Alleghanies, treating of him as he is in himself in his own rights"), "as habitan he him himself his in in is of of own rights the treating I Alleghanies")
test.assert_equals(pseudo_sort("take up the task eternal, and the burden and the lesson"), "and and burden eternal lesson take task the the the up")
test.assert_equals(pseudo_sort("Land of the Old Thirteen! Massachusetts land! land of Vermont and Connecticut!"), "and land land of of the Vermont Thirteen Old Massachusetts Land Connecticut")
test.assert_equals(pseudo_sort("Pioneers, O Pioneers!"), "Pioneers Pioneers O")
test.assert_equals(pseudo_sort("    "), "")
