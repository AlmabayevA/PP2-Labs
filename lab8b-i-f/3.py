s = input()
S = "".join(reversed(s))
if s == S:
    print(s, "is a palindrome")
else:
    print(s, "is not a palindrome")