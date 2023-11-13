import os
path = r'C:\Users\Assan\OneDrive\Desktop\PP2\Lab7\del.py'
if os.access(path,os.F_OK) == True:
    os.remove(path)
    print("The file has been deleted")
else:
    print("The file doesn't exist")