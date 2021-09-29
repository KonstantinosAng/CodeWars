# see https://www.codewars.com/kata/5908242330e4f567e90000a3/train/python

from TestFunction import Test

from math import acos as c;circleIntersection=lambda a,b,r:int(2*r*r*c(((a[0]-b[0])**2+(a[1]-b[1])**2)**.5/(2*r))-.5*(((a[0]-b[0])**2+(a[1]-b[1])**2)*4*r*r-((a[0]-b[0])**2+(a[1]-b[1])**2)**2)**.5)if((a[0]-b[0])**2+(a[1]-b[1])**2)**.5<=2*r else 0

from numpy import*;circleIntersection=lambda a,b,r:r*r*(lambda h:h<1and arccos(h)-h*(1-h*h)**.5)(hypot(*subtract(b,a))/r/2)//.5

test = Test(None)
test.describe("Basic Tests")
test.it("It should works for basic tests.")
test.assert_equals(circleIntersection([0, 0],[7, 0],5),14)
test.assert_equals(circleIntersection([0, 0],[0, 10],10),122)
test.assert_equals(circleIntersection([5, 6],[5, 6],3),28)
test.assert_equals(circleIntersection([-5, 0],[5, 0],3),0)
test.assert_equals(circleIntersection([10, 20],[-5, -15],20),15)
test.assert_equals(circleIntersection([-7, 13],[-25, -5],17),132)
test.assert_equals(circleIntersection([-20, -4],[-40, 29],7),0)
test.assert_equals(circleIntersection([38, -18],[46, -29],10),64)
test.assert_equals(circleIntersection([-29, 33],[-8, 13],15),5)
test.assert_equals(circleIntersection([-12, 20],[43, -49],23),0)
