import os
import string
path = r'C:\Users\Assan\OverDrive\Desktop'
if os.path.exists(path+"\Letters") == False:
    path = os.path.join(path, "Letters\\")
    os.makedirs(path)
    print("Directory has been created")
else:
    print("Directory already exists")
for letter in string.ascii_uppercase:
    with open(path + letter + ".txt", "w") as f:
       f.writelines(letter)