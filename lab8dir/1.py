import os
path = r'C:\Users\Assan\OneDrive\Desktop'
print("Directories:")
print([name for name in os.listdir(path) if os.path.isdir(os.path.join(path, name))])
print("Directories and files:")
print([name for name in os.listdir(path)])
print("Files:")
print([name for name in os.listdir(path) if os.path.isfile(os.path.join(path, name))])