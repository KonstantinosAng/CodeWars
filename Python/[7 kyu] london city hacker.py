# see https://www.codewars.com/kata/5bce125d3bb2adff0d000245/solutions/python

from TestFunction import Test

def london_city_hacker(journey): 
  cost, i = 0.0, 0
  if journey == []: return "£{}".format("%.2f" % cost)
  while i < len(journey):
    if type(journey[i]) == str:
      cost += 2.4
    else:
      if i != len(journey) - 1:
        if type(journey[i+1]) == int:
          i += 1
      cost += 1.5
    i +=1
  return "£{}".format("%.2f" % cost)


Test("£7.80").assert_result(london_city_hacker([12, 'Central', 'Circle', 21]))
Test("£3.90").assert_result(london_city_hacker(['Piccidilly', 56]))
Test("£7.20").assert_result(london_city_hacker(['Northern', 'Central', 'Circle']))
Test("£5.40").assert_result(london_city_hacker(['Piccidilly', 56, 93, 243]))
Test("£3.00").assert_result(london_city_hacker([386, 56, 1, 876]))
Test("£0.00").assert_result(london_city_hacker([]))