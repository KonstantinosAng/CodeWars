# see https://www.codewars.com/kata/5db42a943c3c65001dcedb1a/train/python

def encoder(data):
  dictionary = {0: ""}
  output = ""
  pointer = 0
  index = 1
  flagEnd = False
  while pointer < len(data):
    if data[pointer] not in dictionary:
      dictionary[data[pointer]] = index
      output += f'{0}{data[pointer]}'
      index += 1
      pointer += 1
      flagEnd = False
    else:
      tempWord = data[pointer]
      while tempWord in dictionary:
        pointer += 1
        if pointer >= len(data):
          flagEnd = True
          break
        tempWord += data[pointer]
      if not flagEnd:
        dictionary[tempWord] = index
      else:
        return output + str(dictionary[tempWord])
      output += f'{dictionary[tempWord[:-1]]}{data[pointer] if pointer < len(data) else data[-1]}'
      index += 1
      pointer += 1
  return output

def parse_data(s):
  hashMap = []
  if s[-1].isdigit():
    i = len(s) - 1
    while s[i].isdigit():
      i -= 1
    last = s[i+1:]
    string = s[:i+1]
  else:
    string = s
  start = 0
  end = 0
  while end < len(string):
    while string[end].isdigit():
      end += 1
      if end >= len(string): break
    hashMap.append([s[start:end], s[end]])
    end += 1
    start = end
  return hashMap if not s[-1].isdigit() else hashMap + [[last]]

def decoder(data):
  hashMap = parse_data(data)
  dictionary = {0: ""}
  index = 1
  output = ""
  for item in hashMap:
    if item[0] == '0':
      dictionary[index] = item[1]
      index += 1
    else:
      if len(item) != 1:
        dictionary[index] = dictionary[int(item[0])] + item[1]
      index += 1
  for item in hashMap:
    if len(item) != 1:
      output += dictionary[int(item[0])] + item[1]
    else:
      output += dictionary[int(item[0])]
  return output


from TestFunction import Test
test = Test(None)   
test.describe('Fixed tests')
# test.it('Encoding')
# test.assert_equals(encoder('ABAABABAABAB'), '0A0B1A2A4A4B', 'ABAABABAABAB')
# test.assert_equals(encoder('ABAABABAABABAA'), '0A0B1A2A4A4B3', 'ABAABABAABABAA')
# test.assert_equals(encoder('ABBCBCABABCAABCAABBCAA'), '0A0B2C3A2A4A6B6', 'ABBCBCABABCAABCAABBCAA')
# test.assert_equals(encoder('AAAAAAAAAAAAAAA'), '0A1A2A3A4A', 'AAAAAAAAAAAAAAA')
# test.assert_equals(encoder('ABCABCABCABCABCABC'), '0A0B0C1B3A2C4C7A6', 'ABCABCABCABCABCABC')
# test.assert_equals(encoder('ABCDDEFGABCDEDBBDEAAEDAEDCDABC'), '0A0B0C0D4E0F0G1B3D0E4B2D10A1E4A10D9A2C', 'ABCDDEFGABCDEDBBDEAAEDAEDCDABC')
test.it('Decoding')
# test.assert_equals(decoder('0A0B1A2A4A4B'), 'ABAABABAABAB', '0A0B1A2A4A4B')
# test.assert_equals(decoder('0A0B1A2A4A4B3'), 'ABAABABAABABAA', '0A0B1A2A4A4B3')
# test.assert_equals(decoder('0A0B2C3A2A4A6B6'), 'ABBCBCABABCAABCAABBCAA', '0A0B2C3A2A4A6B6')
# test.assert_equals(decoder('0A1A2A3A4A'), 'AAAAAAAAAAAAAAA', '0A1A2A3A4A')
# test.assert_equals(decoder('0A0B0C1B3A2C4C7A6'), 'ABCABCABCABCABCABC', '0A0B0C1B3A2C4C7A6')
# test.assert_equals(decoder('0A0B0C0D4E0F0G1B3D0E4B2D10A1E4A10D9A2C'), 'ABCDDEFGABCDEDBBDEAAEDAEDCDABC', '0A0B0C0D4E0F0G1B3D0E4B2D10A1E4A10D9A2C')
test.assert_equals(decoder('0N0U0J0G1U3G5J4J0A3A7G11N2J4N13G11'), 'NUJGNUJGNUJGJAJANUJGNUJGNUJGNUJGNUJG', '0A0B0C0D4E0F0G1B3D0E4B2D10A1E4A10D9A2C')
