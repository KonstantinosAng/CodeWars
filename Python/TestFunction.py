from functools import wraps

def test_it(func, parameters, test_case):
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
    finally:
      print("[FUNCTION] {.__name__}".format(func))
      print("Test Case {} resulted in {}". format(test_case, result))
  return test(parameters)