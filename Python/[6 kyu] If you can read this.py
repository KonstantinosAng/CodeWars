# see https://www.codewars.com/kata/5f3afc40b24f090028233490/train/python

from TestFunction import Test

def to_nato(words):
  alphabet = {'A': 'Alfa ',  'B': 'Bravo ',   'C': 'Charlie ',
        'D': 'Delta ',  'E': 'Echo ',    'F': 'Foxtrot ',
        'G': 'Golf ',   'H': 'Hotel ',   'I': 'India ',
        'J': 'Juliett ','K': 'Kilo ',    'L': 'Lima ',
        'M': 'Mike ',   'N': 'November ','O': 'Oscar ',
        'P': 'Papa ',   'Q': 'Quebec ',  'R': 'Romeo ',
        'S': 'Sierra ', 'T': 'Tango ',   'U': 'Uniform ',
        'V': 'Victor ', 'W': 'Whiskey ', 'X': 'Xray ',
        'Y': 'Yankee ', 'Z': 'Zulu ', ' ': ''}
  return "".join(alphabet[c.upper()] if c.upper() in alphabet else f"{c} " for c in words).strip()


test = Test(None)
test.describe("Basic Tests")
test.it("Basic Tests")
test.assert_equals(to_nato('If you can read'), "India Foxtrot Yankee Oscar Uniform Charlie Alfa November Romeo Echo Alfa Delta")
test.assert_equals(to_nato('Did not see that coming'), "Delta India Delta November Oscar Tango Sierra Echo Echo Tango Hotel Alfa Tango Charlie Oscar Mike India November Golf")
test.assert_equals(to_nato('.d?d!'),'. Delta ? Delta !')
