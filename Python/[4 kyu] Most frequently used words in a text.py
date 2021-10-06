# see https://www.codewars.com/kata/51e056fe544cf36c410000fb/train/python

def top_3_words(text):
  retDict = {}
  text = "".join(x if x.isalpha() or x == "'" else " " for x in text)
  # print(text)
  for word in text.split(" "):
    if "".join(x for x in word if x.isalpha()).isalpha():
      word = "".join(x for x in word if x.isalpha() or x == "'")
      if word in retDict: retDict[word] += 1
      else: retDict[word] = 1
  retArray = []
  retDict = {key:value for key, value in sorted(retDict.items(), key=lambda x: len(x[0]))}
  # print(retDict)
  while len(retDict) > 0 and len(retArray) < 3:
    # print(retDict)
    currentMaxWord = max(retDict.items(), key=lambda x: x[1])
    retArray.append(currentMaxWord[0].lower())
    retDict = {key:value for key, value in retDict.items() if key != currentMaxWord[0]}
  # print(retArray)
  return retArray
  

from TestFunction import Test

test = Test(None)

test.assert_equals(top_3_words("dwhehI  ?-dwhehI:://dwhehI!dwhehI!//:dwhehI/?/dwhehI:!-dwhehI-_,dwhehI:-dwhehI/dwhehI?-:-dwhehI_dwhehI.dwhehI.,;dwhehI:, :.dwhehI,_;:dwhehI?!,,dwhehI.?_.dwhehI :dwhehI!_,;dwhehI!/dwhehI?dwhehI:-dwhehI_dwhehI :/:_dwhehI;!.-dwhehI !! .dwhehI-?:dwhehI;.dwhehI/! /dwhehI.!:/"), ['dwhehi'])
# test.assert_equals(top_3_words("a a a'  b  c, c  d d d d  e e e e e"), ["e", "d", "a"])
# test.assert_equals(top_3_words("a a a  b  c c  d d d d  e e e e e"), ["e", "d", "a"])
# test.assert_equals(top_3_words("e e e e DDD ddd DdD: ddd ddd aa aA Aa, bb cc cC e e e"), ["e", "ddd", "aa"])
# test.assert_equals(top_3_words("  //wont won't won't "), ["won't", "wont"])
# test.assert_equals(top_3_words("  , e   .. "), ["e"])
# test.assert_equals(top_3_words("  ...  "), [])
# test.assert_equals(top_3_words("  '  "), [])
# test.assert_equals(top_3_words("  '''  "), [])
# test.assert_equals(top_3_words("""In a village of La Mancha, the name of which I have no desire to call to
# mind, there lived not long since one of those gentlemen that keep a lance
# in the lance-rack, an old buckler, a lean hack, and a greyhound for
# coursing. An olla of rather more beef than mutton, a salad on most
# nights, scraps on Saturdays, lentils on Fridays, and a pigeon or so extra
# on Sundays, made away with three-quarters of his income."""), ["a", "of", "on"])