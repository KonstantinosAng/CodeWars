# see https://www.codewars.com/kata/5a1ebc2480171f29cf0000e5/solutions/python

from TestFunction import test_it
from math import pi

def sort_by_area(seq): 
    areas = []
    for item in seq:
      if type(item) == tuple:
        areas.append([item, item[0]*item[1]])
      else:
        areas.append([item, pi*item*item])
    return [shape[0] for shape in sorted(areas, key=lambda x: x[1])]

test_it(sort_by_area, [ (4.23, 6.43), 1.23, 3.444, (1.342, 3.212) ], [ (1.342, 3.212), 1.23, (4.23, 6.43), 3.444 ])
test_it(sort_by_area, [ (2, 5), 6 ], [ (2, 5), 6 ])
test_it(sort_by_area, [], [] )
