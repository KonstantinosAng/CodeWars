# see https://www.codewars.com/kata/5e7837d0262211001ecf04d7/solutions/python

from TestFunction import Test


def html(*args, **kwargs):
  keywords, elements = [], []
  if kwargs:
    for key, value in kwargs.items():
      if key == "cls":
        key = 'class'
      keywords.append(f'{key}="{value}"')
  if len(args) == 1:
    if kwargs:
      element = f'<{args[0]}'
      for key in keywords:
          element += ' ' + key
      element += ' />'
      return element
    else:
      return f'<{args[0]} />'
  for i, arg in enumerate(args):
    if i == 0: tag = arg
    else:
      element = f'<{tag}'
      if kwargs:
        for key in keywords:
          element += ' ' + key
      element += f'>{arg}</{tag}>' 
      elements.append(element)
  return "\n".join(element for element in elements)


test = Test(None)
test.assert_equals(html('img', src="/images/img.png"), '<img src="/images/img.png" />')
test.assert_equals(html('br'), '<br />')
test.assert_equals(html('p', 'Hello World!', 'This is html code!', cls="paragraph-text", id="example"), '<p class="paragraph-text" id="example">Hello World!</p>\n<p class="paragraph-text" id="example">This is html code!</p>')
test.assert_equals(html('form', 'Some text in here, too', method='post', action='somefile.php'), '<form method="post" action="somefile.php">Some text in here, too</form>')
test.assert_equals(html('input', type='text', id="thisinput", name="InsertName", size="50"), '<input type="text" id="thisinput" name="InsertName" size="50" />')
test.assert_equals(html('span', 'This text would be red', cls="span1", style="color: red;", role="main"), '<span class="span1" style="color: red;" role="main">This text would be red</span>')
test.assert_equals(html('title', 'Webpage Title'), '<title>Webpage Title</title>')
test.assert_equals(html('ul', "This would be <li> elements.", cls="list"), '<ul class="list">This would be <li> elements.</ul>')
test.assert_equals(html("table", "    ", border="1 px solid gold"), '<table border="1 px solid gold">    </table>')
test.assert_equals(html("h1", "This is a header", randomattributename="randomattributevalue"), '<h1 randomattributename="randomattributevalue">This is a header</h1>')
