# see https://www.codewars.com/kata/56b3b27cadd4ad275500000c/train/python

def filterFunction(x):
  filters = ['a', 'the', 'on', 'at', 'of', 'in', 'as']
  if x.lower() in filters: 
    return False
  return True

def word_count(s):
  counter = 0
  retArray = []
  while counter < len(s):
    if s[counter].isalpha():
      tempCounter = counter
      while s[counter].isalpha():
        counter += 1
        if counter >= len(s): break
      retArray.append(s[tempCounter:counter])
    counter += 1
  retArray = [x for x in filter(filterFunction, retArray)]
  return len(retArray)

from TestFunction import Test
test = Test(None)
test.describe("Fixed Tests")
test.it("Short Text")
test.assert_equals(word_count("hello there"), 2)
test.assert_equals(word_count("hello there and a hi"), 4)
test.assert_equals(word_count("I'd like to say goodbye"), 6)
test.assert_equals(word_count("Slow-moving user6463 has been here"), 6)
test.assert_equals(word_count("%^&abc!@# wer45tre"), 3)
test.assert_equals(word_count("abc123abc123abc"), 3)
test.assert_equals(word_count("Really2374239847 long ^&#$&(*@# sequence"), 3)
test.it("Long text")
long_text = """
I’d been using my sphere as a stool. I traced counterclockwise circles on it with my fingertips and it shrank until I could palm it. My bolt had shifted while I’d been sitting. I pulled it up and yanked the pleats straight as I careered around tables, chairs, globes, and slow-moving fraas. I passed under a stone arch into the Scriptorium. The place smelled richly of ink. Maybe it was because an ancient fraa and his two fids were copying out books there. But I wondered how long it would take to stop smelling that way if no one ever used it at all; a lot of ink had been spent there, and the wet smell of it must be deep into everything.
"""
test.assert_equals(word_count(long_text), 112)
long_text = """
The Mynster had a ceiling of stone, steeply vaulted. Above the vaults, a flat roof had been framed. Built upon that roof was the aerie of the Warden Fendant. Its inner court, squared around the Præsidium, was roofed and walled and diced up into store-rooms and headquarters, but its periphery was an open walkway on which the Fendant’s sentinels could pace a full circuit of the Mynster in a few minutes’ time, seeing to the horizon in all directions (except where blocked by a buttress, pier, spire, or pinnacle). This ledge was supported by dozens of close-spaced braces that curved up and out from the walls below. The end of each brace served as a perch for a gargoyle keeping eternal vigil. Half of them (the Fendant gargoyles) gazed outward, the other half (the Regulant gargoyles) bent their scaly necks and aimed their pointy ears and slitted eyes into the concent spread below. Tucked between the braces, and shaded below the sentinels’ walkway, were the squat Mathic arches of the Warden Regulant’s windows. Few places in the concent could not be spied on from at least one of these— and, of course, we knew them all by heart.
"""
test.assert_equals(word_count(long_text), 160)