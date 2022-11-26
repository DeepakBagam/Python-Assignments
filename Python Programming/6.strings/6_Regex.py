import re

txt = "hello every one"
match = re.match("hello", txt)

if match:
  print("regex matches: ", match.group())
else:
  print('pattern not found')
