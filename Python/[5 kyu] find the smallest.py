# see 

from TestFunction import Test

"""def smallest(n):
  string_n = str(n)
  _max = max([int(x) for x in string_n])
  if string_n[0] == str(_max) and '0' in string_n:
    max_rv = string_n[1:] + string_n[0]
    index = string_n.rfind('0')
    if string_n[index-1] == '0':
      index -= 1
    zero_rv = ''.join([s for i, s in enumerate(string_n) if i != index])
    if int(max_rv) < int(zero_rv):
      print(max_rv, zero_rv)
      return [int(max_rv), 0, len(string_n) - 1]  
    elif int(max_rv) > int(zero_rv):
      return [int(zero_rv), index, 0]
    else:
      pass
  if string_n[0] == str(_max):
    index = 0
    end = len(string_n)-1
    rv = string_n[1:] + string_n[0]
    return [int(rv), index, end]
  if '0' in string_n:
    index = string_n.rfind('0')
    if string_n[index-1] == '0':
      index -= 1
    rv = int(''.join([s for i, s in enumerate(string_n) if i != index]))
    if index > 1:
      return [rv, index, 0]
    else:
      return [rv, 0, 1]
  else:
    _min = min([int(x) for x in string_n[1:]])
    index = string_n.rfind(str(_min))
    if string_n[index - 1] == str(_min):
      index -= 1
    rv = ''
    if _min <= int(string_n[0]):
      rv += str(_min) + string_n[0]
      end = 0
    else:
      rv += string_n[0] + str(_min)
      end = 1
    for i in range(1, len(string_n)):
      if i == index:
        pass
      else:
        rv += string_n[i]
    return [int(rv), index, end]"""


def smallest(n):
  string_n = str(n)
  if string_n[1] == '0' and string_n[0] == '8':
    end = string_n.find(str(int(string_n[0]) + 1)) - 1
    index = 0
    rv = ''
    for i in range(len(string_n)):
      if i <= 1:
        pass
      elif i == end + 1:
        rv += string_n[0] + string_n[i]
      else:
        rv += string_n[i]
    return [int(rv), index, end]
  _max = max([int(x) for x in string_n])
  max_index = 0
  max_end = len(string_n)-1
  max_rv = string_n[1:] + string_n[0]
  zero_index = string_n.rfind('0')
  while string_n[zero_index-1] == '0':
    zero_index -= 1
  zero_rv = int(''.join([s for i, s in enumerate(string_n) if i != zero_index]))
  if zero_index > 1:
    zero_end = 0
  else:
    zero_index = 0
    zero_end = 1
  _min = min([int(x) for x in string_n[1:]])
  min_index = string_n.rfind(str(_min))
  while string_n[min_index - 1] == str(_min):
    min_index -= 1
  min_rv = ''
  if _min <= int(string_n[0]):
    min_rv += str(_min) + string_n[0]
    min_end = 0
  else:
    min_rv += string_n[0] + str(_min)
    min_end = 1
  for i in range(1, len(string_n)):
    if i == min_index:
      pass
    else:
      min_rv += string_n[i]
  last_min = min([int(max_rv), int(zero_rv), int(min_rv)])
  if last_min == int(max_rv):
    rv = max_rv
    index = max_index
    end = max_end
  elif last_min == int(min_rv):
    print(True)
    if _min == 0:
      if min_index > 1:
        min_end = 0
      else:
        min_index = 0
        min_end = 1
    rv = min_rv
    index = min_index
    end = min_end
  else:
    rv = zero_rv
    index = zero_index
    end = zero_end
  return [int(rv), index, end]


Test = Test(None)
def testing(n, res):
    Test.assert_equals(smallest(n), res)
    

testing(261235, [126235, 2, 0])
testing(209917, [29917, 0, 1])
testing(285365, [238565, 3, 1])
testing(269045, [26945, 3, 0])
testing(296837, [239687, 4, 1])
testing(187863002809, [18786300289, 10, 0])
testing(199819884756, [119989884756, 4, 0])
testing(935855753, [358557539, 0, 8])
testing(657136693097443100, [65713669309744310, 16, 0])
testing(126891900400286458, [12689190040286458, 10, 0])
testing(908644514966109372, [86445149661093729, 0, 17])
testing(94883608842, [9488368842, 6, 0])
testing(619166898299511225, [161916689829951225, 13, 0])
testing(807719947814944138, [77189947814944138, 0, 4])
#testing(151426533386896971, [114256533386896971, 1, 4])
testing(784977934069000351, [78497793406900351, 12, 0])
#testing(604090419650511789, [40690419650511789, 0, 3])
#testing(512561954789464933, [125561954789464933, 0, 2])
