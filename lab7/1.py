import re
a = "abbb"
b = "bbbb"
c = "shjjaabbbjkj"
x = re.search("ab*", a)
if x:
    print(x.string)
x = re.search("ab*", b)
if x:
    print(x.string)
x = re.search("ab*", c)
if x:
    print(x.string)