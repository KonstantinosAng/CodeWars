from functools import wraps


class Test:

  def __init__(self, tests):
    self.test_case = tests
    self.result = None

  def it(self, *args, **kwargs):
    for arg in args:
      if type(arg) == str:
        print("")
        print(arg)
        print("-"*len(arg))

  def describe(self, *args, **kwargs):
    for arg in args:
      if type(arg) == str:
        print("")
        print(arg)
        print("-"*len(arg))

  def assert_result(self, *args):
    print("Test Case {} resulted in {} {}". format(self.test_case, args[0], "✅" if args[0]==self.test_case else "❌"))
  
  def assert_equals(self, *args, **kwargs):
    print("Test Case {} resulted in {} {}". format(args[1], args[0], "✅" if args[0]==args[1] else "❌"))

  def expect(self, *args, **kwargs):
    print("Test Case {} resulted in {}". format(args[0], "✅" if args[0] else "❌"))


def Tester(test_case, *args, **kwargs):

  def test_it(func):
    """
    Test any function with test units
    :param func: any python function
    :return: None
    """
    @wraps(func)
    def test(*args, **kwargs):
      """
      execute function and test it
      :param args: any argument
      :param kwargs: any keyword argument
      :return: None
      """
      try:
        ret = func(*args, **kwargs)
        result = ret == test_case
        return result
      except Exception as e:
        print("[TEST CASE: ({.__name__}) ] {} ❗❗❗".format(func, e))
      finally:
        if result is not None:
          print("[FUNCTION] {.__name__} ➡ [TEST CASE] {}".format(func, test_case))
          print("Test Case resulted in {} {}". format(ret, "✅" if result else "❌"))
    return test(*args, **kwargs)
  return test_it
 