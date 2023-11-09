import re

txt = "snake_case_Sample"
x = re.split("_", txt)
for i in range(len(x)):
    x[i] = x[i].capitalize()
s = "".join(x)
print(s)