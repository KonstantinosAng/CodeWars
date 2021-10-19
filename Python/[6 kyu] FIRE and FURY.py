# see https://www.codewars.com/kata/59922ce23bfe2c10d7000057/train/python

def fire_and_fury(tweet):
  booleans = [True if x in ['F', 'I', 'R', 'E', 'U', 'Y'] else False for x in tweet]
  if False in booleans: return "Fake tweet."
  pointer = 0
  retArray = []
  tempWord = ("", 0)
  while pointer + 3 < len(tweet):
    string = tweet[pointer:pointer + 4]
    if string in ['FURY', 'FIRE']:
      if tempWord[0] == "":
        tempWord = (string, tempWord[1]+1)
      else:
        if string == tempWord[0]:
          tempWord = (string, tempWord[1]+1)
        else:
          if tempWord[0] == 'FURY':
            retArray.append("I am " + 'really '*(tempWord[1]-1) + "furious.")
          else:
            retArray.append("You " + 'and you '*(tempWord[1]-1) + "are fired!")
          tempWord = (string, 1)
    pointer += 1
  if tempWord[0] != "":
    if tempWord[0] == 'FURY':
      retArray.append("I am " + 'really '*(tempWord[1]-1) + "furious.")
    else:
      retArray.append("You " + 'and you '*(tempWord[1]-1) + "are fired!")
    return " ".join(x for x in retArray)
  return "Fake tweet."
    


from TestFunction import Test
test = Test(None)

test.describe("Sample tests")
test.it("Ex1")
test.assert_equals(fire_and_fury("FURYYYFIREYYFIRE"), "I am furious. You and you are fired!")
print('<COMPLETEDIN::>')

test.it("Ex2")
test.assert_equals(fire_and_fury("FIREYYFURYYFURYYFURRYFIRE"), "You are fired! I am really furious. You are fired!")
print('<COMPLETEDIN::>')

test.it("Ex3")
test.assert_equals(fire_and_fury("FYRYFIRUFIRUFURE"), "Fake tweet.")
print('<COMPLETEDIN::>')
print('<COMPLETEDIN::>')