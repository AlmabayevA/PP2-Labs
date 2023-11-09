import re
a = "aaaab"
b = "bhgabbd"
c = "abbbb"
d = "nhshjabbbjhhb"
x = re.search("abb[^b]|abbb[^b]", a)
if x:
    print(x.string)
x = re.search("abb[^b]|abbb[^b]", b)
if x:
    print(x.string)
x = re.search("abb[^b]|abbb[^b]", c)
if x:
    print(x.string)
x = re.search("abb[^b]|abbb[^b]", d)
if x:
    print(x.string)