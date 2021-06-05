print("Enter the value1 :")
n1 = input()
print("Enter the value2 :")
n2 = input()
# print("this of these two number is " , int(n1)+int(n2))


try:
    print("this of these two number is " , int(n1)+int(n2))
except Exception as e:
    print(e)
print("This line are important")        