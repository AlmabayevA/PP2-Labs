s = input()
s_upper = sum(1 for l in s if l.isupper())
s_lower = sum(1 for l in s if l.islower())
print("upper:", s_upper, "lower:", s_lower)