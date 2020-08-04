# see https://www.codewars.com/kata/5e882048999e6c0023412908/solutions/python

from TestFunction import Test


class DefaultList:

  def __init__(self, lst, value):
    self.lst = lst
    self.default = value

  def __getitem__(self, item):
    try:
      return self.lst[item]
    except:
      return self.default

  def extend(self, *args):
    for x in args:
      self.lst.extend(x)

  def append(self, *args):
    for x in args:
      self.lst.append(x)

  def insert(self, *args):
    self.lst.insert(args[0], args[1])

  def remove(self, *args):
    for x in args:
      self.lst.remove(x)

  def pop(self, *args):
    for x in args:
      self.lst.pop(x)


test = Test(None)
lst = DefaultList([1, 3, 4, 7, 2, 34], 'def')

test.assert_equals(lst[1], 3)
test.assert_equals(lst[333000], 'def')
test.assert_equals(lst[23], 'def')

lst.extend([3, 23, 'hello', 'lists', 'word', 344])

test.assert_equals(lst[9], 'lists')
test.assert_equals(lst[11], 344)
test.assert_equals(lst[12], 'def')

lst.append(233344455)

test.assert_equals(lst[12], 233344455)
test.assert_equals(lst[100], 'def')

lst.remove(2)
lst.remove(1)
lst.remove(3)

lst.insert(-3, 34.34)
test.assert_equals(lst[8], 'word')
test.assert_equals(lst[10], 233344455)
