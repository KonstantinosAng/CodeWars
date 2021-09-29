# see https://www.codewars.com/kata/5f3afc40b24f090028233490/train/python

from TestFunction import Test

def swap(s,n):
  if n == 0: return s
  if s == "" : return ""
  binary = str(bin(n))[2:]
  binary = binary*(int((len(s)/len(binary)))+1)
  ret = ''
  pointerSentence = 0
  pointerBinary = 0 
  while pointerSentence < len(s):
    c = s[pointerSentence]
    if c.isalpha() and binary[pointerBinary] == '1':
      if c.lower() == c:
        ret += c.upper()
      else:
        ret += c.lower()
    else:
      ret += c
    pointerSentence += 1
    if c.isalpha():
      pointerBinary += 1
  return ret

test = Test(None)
test.it('Basic Test Cases')
test.assert_equals(swap('Hello world!', 11), 'heLLO wORLd!')
test.assert_equals(swap('the quick broWn fox leapt over the fence',9),'The QUicK BrowN foX LeaPT ovER thE FenCE')
test.assert_equals(swap('eVerybody likes ice cReam',85),'EVErYbODy LiKeS IcE creAM')
test.assert_equals(swap('gOOd MOrniNg',7864),'GooD MorNIng')
test.assert_equals(swap('how are you today?',12345),'HOw are yoU TOdaY?')    
test.it('Edge Cases')
test.assert_equals(swap('the lord of the rings', 0), 'the lord of the rings')
test.assert_equals(swap('',11345),'')

