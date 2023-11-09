import re

a = "gggahdjdj&&&-7667775b"
b = "aaaaa"
c = "ab"
d = "abbc"
x = re.search(r"a.*b\b", a)
if x:
    print(x.string)
x = re.search(r"a.*b\b", b)
if x:
    print(x.string)
x = re.search(r"a.*b\b", c)
if x:
    print(x.string)
x = re.search(r"a.*b\b", d)
if x:
    print(x.string)
