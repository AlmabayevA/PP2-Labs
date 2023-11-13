import os
path = r'C:\Users\Assan\OneDrive\Desktop\PP2\Lab7\1.py'
f = open(path)
cnt = 0
for line in f:
    cnt += 1
print("There are", cnt, "lines in", os.path.basename(path), "file")