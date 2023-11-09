import re

a = "sdjhHHHmsgkLnsnn"
b = "ViktoriyaKalashnikova"
c = "nothing_to_split"

x= re.split(r"(?=[A-Z])", a)
if x[0] == "":    
    x.pop(0)
s = " ".join(x)
print(s)
x= re.split(r"(?=[A-Z])", b)
if x[0] == "":    
    x.pop(0)
s = " ".join(x)
print(s)
x= re.split(r"(?=[A-Z])", c)
if x[0] == "":    
    x.pop(0)
s = " ".join(x)
print(s)
