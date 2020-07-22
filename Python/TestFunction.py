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
    result = None
    try:
      result = func(*args, **kwargs) == test_case
      return result
    except Exception as e:
      print("[TEST CASE: ({.__name__}) ] {} ❗❗❗".format(func, e))
    finally:
      if result is not None:
        print("[FUNCTION] {.__name__} ➡ [TEST CASE] {}".format(func, test_case))
        if result:
          print("Test Case resulted in {} ✅". format(result))
        else:
          print("Test Case resulted in {} ❌". format(result))
  return test(parameters)