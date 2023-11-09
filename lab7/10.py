import re

txt = "CamelCaseSample"

x= re.split(r"(?=[A-Z])", txt)
x.pop(0)
for i in range(len(x)):
    x[i] = x[i].lower()
    
s = "_".join(x)
print(s)