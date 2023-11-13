import os
path = r'C:\Users\Assan\OneDrive\Desktop\PP2'
if (os.access(path, os.X_OK) == True):
    print("The path exists")
    print("The file name is", os.path.basename(path))
    print("The directory portion is", os.path.dirname(path))
else:
    print("The path doesn't exist")
