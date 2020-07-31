# see 

"""
!!!!!!!!!! NOT SOLVED !!!!!!!!!!!!! 
"""

from TestFunction import Test

def mystery_range(s, n):
  i, j = 0, n - 1
  found = False
  stop = False
  while not found and not stop:
    string = str(s)
    for number in range(i, j):
      if str(number) not in string:
        found = True
        stop = False
        break
      else:
        string.replace(str(number), '', 1)
        print(string)
    if found:
      found = False
      i += 1
      j += 1
    else:
      stop = True
  return [i, j]

test = Test(None)

example_tests = (
	(('6291211413114538107',14),[1,14]),
	#(('13161820142119101112917232215',15),[9,23]),
	#(('2318134142120517221910151678611129',20),[4,23]),
	#(('10610211511099104113100116105103101111114107108112109',18),[99,116]),
	#(('1721532418565922162558663126649136347436733301144143236653738464135820194215516155541239452852623450572927602348104049',60),[8,67])
)
for inp,out in example_tests:
	test.assert_equals(mystery_range(*inp),out)
