import re

a = "djhhbdHdhkmshKhhgd397"
b = "ViktoriyaKalashnikova"
x= re.findall("[A-Z][a-z]+", a)
if x:
    print(x)
x= re.findall("[A-Z][a-z]+", b)
if x:
    print(x)