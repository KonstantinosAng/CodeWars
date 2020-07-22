from functools import wraps


class Test:

  def __init__(self, tests):
    self.test_cases = tests
    self.result = None

  def assert_result(self, result):
    print("Test Case resulted in {} {}". format(result, "✅" if result==self.test_case else "❌"))


def Tester(test_case):

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
        result = func(*args, **kwargs) == test_case
        return result
      except Exception as e:
        print("[TEST CASE: ({.__name__}) ] {} ❗❗❗".format(func, e))
      finally:
        if result is not None:
          print("[FUNCTION] {.__name__} ➡ [TEST CASE] {}".format(func, test_case))
          print("Test Case resulted in {} {}". format(result, "✅" if result else "❌"))
    return test
  return test_it
