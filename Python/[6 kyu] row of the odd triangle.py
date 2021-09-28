# see https://www.codewars.com/kata/5d5a7525207a674b71aa25b5/train/python

from TestFunction import Test

def odd_row(n):
  if n == 1: return [1]
  start = sum(x for x in range(n))
  stop = sum(x for x in range(n+1))
  range_start = sum([2*x for x in range(n)]) + 1
  return [range_start+x for x in range(0, 2*(stop-start), 2)]

test = Test(None)
test.assert_equals(odd_row(1), [1])
test.assert_equals(odd_row(2), [3, 5])

test.assert_equals(odd_row(13), [157, 159, 161, 163, 165, 167, 169, 171,
    173, 175, 177, 179, 181])

test.assert_equals(odd_row(19), [343, 345, 347, 349, 351, 353, 355, 357,
    359, 361, 363, 365, 367, 369, 371, 373, 375, 377, 379])

test.assert_equals(odd_row(41), [1641, 1643, 1645, 1647, 1649, 1651, 1653,
    1655, 1657, 1659, 1661, 1663, 1665, 1667, 1669, 1671, 1673, 1675, 1677,
    1679, 1681, 1683, 1685, 1687, 1689, 1691, 1693, 1695, 1697, 1699, 1701,
    1703, 1705, 1707, 1709, 1711, 1713, 1715, 1717, 1719, 1721])