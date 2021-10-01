# see https://www.codewars.com/kata/514a024011ea4fb54200004b/train/python

def domain_name(url):
  print(url.split("."))
  parsed = url.split('.')
  if parsed[0][:3] == 'htt':
    if parsed[0].split("//")[1] == 'www': return parsed[1]
    if 'https' in parsed[0]: 
      parsed[0] = parsed[0][8:]
    if 'http' in parsed[0]:
      parsed[0] = parsed[0][7:]
    return parsed[0]
  if parsed[0][:3] == 'www':
    return parsed[1]
  return parsed[0]


from TestFunction import Test
test = Test(None)   

test.assert_equals(domain_name("http://google.com"), "google")
test.assert_equals(domain_name("http://google.co.jp"), "google")
test.assert_equals(domain_name("www.xakep.ru"), "xakep")
test.assert_equals(domain_name("xakep.ru"), "xakep")
test.assert_equals(domain_name("https://youtube.com"), "youtube")
test.assert_equals(domain_name("http://www.codewars.com/kata/"), "codewars")