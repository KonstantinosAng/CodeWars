# see https://www.codewars.com/kata/52763db7cffbc6fe8c0007f8/train/python

def isUpper(letter):
  return letter.upper() == letter

def tongues(code):
  words = code.split(" ")
  vowelsMap = ['a', 'i', 'y', 'e', 'o', 'u']
  consonantsMap = ['b', 'k', 'x', 'z', 'n', 'h', 'd', 'c', 'w', 'g', 'p', 'v', 'j', 'q', 't', 's', 'r', 'l', 'm', 'f']
  retArray = []
  for word in words:
    decodedWord = ""
    for letter in word:
      if letter.isalpha():
        if letter.lower() in vowelsMap:
          index = vowelsMap.index(letter.lower()) - 3
          newLetter = vowelsMap[index]
        else:
          index = consonantsMap.index(letter.lower()) - 10
          newLetter = consonantsMap[index]
        if isUpper(letter): decodedWord += newLetter.upper()
        else: decodedWord += newLetter
      else:
        decodedWord += letter
    retArray.append(decodedWord)
  # print(retArray)
  return " ".join(x for x in retArray)
    
    
  

from TestFunction import Test
test = Test(None)

test.assert_equals(tongues('Ita dotf ni dyca nsaw ecc.'), 'One ring to rule them all.')
test.assert_equals(tongues('Tim oh nsa nowa gid ecc fiir wat ni liwa ni nsa eor ig nsaod liytndu.'), 'Now is the time for all good men to come to the aid of their country.')
test.assert_equals(tongues('Giydhlida etr hakat uaedh efi iyd gidagensadh pdiyfsn ytni nsoh'), 'Fourscore and seven years ago our forefathers brought unto this')
test.assert_equals(tongues('litnotatn e tam tenoit.'), 'continent a new nation.')
test.assert_equals(tongues('Nsa zyolv pdimt gij xywbar ikad nsa cequ rifh.'), 'The quick brown fox jumped over the lazy dogs.')