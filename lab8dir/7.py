import os
path1 = r'C:\Users\Assan\OneDrive\Desktop\PP2\Lab7\2.txt'
path2 = r'C:\Users\Assan\OneDrive\Desktop\PP2\Lab7\3.txt'
f1 = open(path1)
f2 = open(path2, 'w')
for line in f1:
    f2.write(line)