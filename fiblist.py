def fib1(n):

    result = []
    a,b = 0, 1
    while a<n:
        result.append(a)
        a,b =b,a+b
       
    return result    
f1 = fib1(100)
print(f1)