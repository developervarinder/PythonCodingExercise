# import os

# cwd = os.getcwd()

# files=os.listdir(cwd)
# print("files in %cler: %s " %(cwd,files))



f =  open("/home/varinder/Development/Python_Projects/PythonCodingExercise/varinder.txt", "rt") # fetching file path using OPEN function

print(f.readlines())
# print(f.readline())
# print(f.readline())
# content = f.read(6484643) # read the content using READ function

# for line in f:

#     print(line,  end ="")



# content = f.read(6484643) # read the content using READ function
# print("1",content) 

# content = f.read(6484643) # read the content using READ function
# print("2",content) 

f.close()  # closing the open file CLOSE