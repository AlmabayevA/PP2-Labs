from datetime import date

d = date(2023, 10, 27)
d2 = date(2023, 11, 27)
delta = d2 - d
print(delta.days * 24 * 3600)