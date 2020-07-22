# see https://www.codewars.com/kata/5296455e4fe0cdf2e000059f/solutions/python

from TestFunction import Test

def calculate(num1, operation, num2): 
    if operation == "+":
      return num1 + num2
    elif operation == "-":
      return num1 - num2
    elif operation == "*":
      return num1*num2
    elif operation == "/":
      return num1/num2 if num2 != 0 else None
    else:
      return None

Test(11.2).assert_result(calculate(3.2,"+", 8))
Test(-4.8).assert_result(calculate(3.2,"-", 8))
Test(0.4).assert_result(calculate(3.2,"/", 8))
Test(25.6).assert_result(calculate(3.2,"*", 8))
Test(-3).assert_result(calculate(-3,"+", 0))
Test(-3).assert_result(calculate(-3,"-", 0))
Test(1).assert_result(calculate(-2, "/", -2))
Test(0).assert_result(calculate(-3,"*", 0))
Test(None).assert_result(calculate(-3,"/", 0))
Test(None).assert_result(calculate(-3,"w", 0))
Test(None).assert_result(calculate(-3,"w", 1))