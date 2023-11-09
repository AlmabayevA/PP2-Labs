import re

a = "66djnh_nsjGGKJHv098_hgaj_kk_L"
b = "Viktoriya_kalashnikova_age_19"

x= re.findall(r"([a-z]+_)([a-z]*_)*([a-z]+)", a)
if x:
    for i in x:
        s = "".join(i)
        print(s)

x= re.findall(r"([a-z]+_)([a-z]*_)*([a-z]+)", b)
if x:
    for i in x:
        s = "".join(i)
        print(s)