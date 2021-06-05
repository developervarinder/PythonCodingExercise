# import os

# cwd = os.getcwd()

# files=os.listdir(cwd)
# print("files in %r: %s " %(cwd,files))



f =  open("/home/varinder/Pythondocs/varinder.txt", "rt") # fetching file path using OPEN function
content = f.read() # read the content using READ function
print(content) 

f.close()  # closing the open file CLOSE