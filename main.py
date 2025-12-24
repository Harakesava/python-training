# version 1
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
