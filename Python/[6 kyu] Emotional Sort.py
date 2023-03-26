# see https://www.codewars.com/kata/5f3afc40b24f090028233490/train/python

from TestFunction import Test

def sort_emotions(arr, order):
  emotions = {'T_T': 4, ':D': 0, ':|': 2, ':)': 1, ':(': 3}
  return sorted(arr, key = lambda x: emotions[x], reverse=not order)


test = Test(None)
test.describe("Basic Tests")    
test.it("Descending")
test.assert_equals(sort_emotions([ ':D', 'T_T', ':D', ':(' ], True), [ ':D', ':D', ':(', 'T_T' ])
test.assert_equals(sort_emotions([ 'T_T', ':D', ':(', ':(' ], True), [ ':D', ':(', ':(', 'T_T' ])
test.assert_equals(sort_emotions([ ':)', 'T_T', ':)', ':D', ':D' ], True), [ ':D', ':D', ':)', ':)', 'T_T' ])

test.it("Ascending")
test.assert_equals(sort_emotions([ ':D', 'T_T', ':D', ':(' ], False), [ 'T_T', ':(', ':D', ':D' ])
test.assert_equals(sort_emotions([ 'T_T', ':D', ':(', ':(' ], False), [ 'T_T', ':(', ':(', ':D' ])
test.assert_equals(sort_emotions([ ':)', 'T_T', ':)', ':D', ':D' ], False),  [ 'T_T', ':)', ':)', ':D', ':D' ])

test.it("Empty array")
test.assert_equals(sort_emotions([], False), [])
test.assert_equals(sort_emotions([], True), [])
