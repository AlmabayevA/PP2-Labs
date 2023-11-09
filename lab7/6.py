import re

a = "a,b    c.f"
b = "hi,i am vika. how are u?"
c = "nosigntoreplace"

x = re.sub("\s|,|[.]", ":", a)
print(x)
x = re.sub("\s|,|[.]", ":", b)
print(x)
x = re.sub("\s|,|[.]", ":", c)
print(x)
