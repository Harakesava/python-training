# version 1 fizzbuzz problem
x=int(input('enter the number:'))
for i in range(1,x+1):
    
    if (i%3==0) and (i%5==0):
        
        print("fizzbuzz")
    elif (i%5==0):
        print("buzz")
    elif (i%3==0):
        print("fizz")
    else:
        print(i)

#version 2 fizzbuzz problem
x=int(input('enter the number:'))
for i in range(1,x+1):
    
    if (i%3==0) :
        if (i%5==0):
        print("fizzbuzz")
    elif (i%5==0):
        print("buzz")
    elif (i%3==0):
        print("fizz")
    else:
        print(i)
