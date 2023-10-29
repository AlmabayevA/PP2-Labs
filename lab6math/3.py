import math 

s = int(input()) #sides
L = int(input()) #length of sides

print ((s*L * (L / (2 * math.tan(math.pi/s))))/2)