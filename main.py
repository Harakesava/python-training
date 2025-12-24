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

#square pattern
x=int(input("enter a number:"))
for i in range (x):
    for j in range (x):
        print ("*",end=' ')
    print ()

#right angle triangle pattern
x=int(input("enter a number:"))
for i in range (x):
    for j in range (i+1):
        print ("*", end=" ")
    print (  )
    
#number pattern
x=int(input("enter a number:"))
for i in range (x):
    for j in range (i+1):
        print (j,end=" " )
    print()

#pyramidal pattern 1
x=int(input("enter a number:"))
for i in range (x):
    for j in range (x-i-1):
        print (" ",end='')
    for j in range (i+1):
        print ("*", end=" ")
    print()

#pyramidal pattern 2
x=int(input("enter a number:"))
for i in range (x):
    for j in range (x-i-1):
        print (" ",end='')
    for j in range (2*i+1):
        print ("*", end="")
    print()

#diamond pattern
x=int(input("enter a number:"))
for i in range (x):
    for j in range (x-i-1):
        print (" ",end='')
    for j in range (i+1):
        print ("*", end=" ")
    print()
for i in range (x-2,-1,-1):
    for j in range (x-i-1):
        print (" ",end='')
    for j in range (i+1):
        print ("*",end=' ')
    print()

#hallow square
n=int(input("enter a number:"))
for i in range (n):
    for j in range (n):
        if i==0 or j==0 or i==n-1 or j==n-1:
            print ("*",end=' ')
        else :
            print (" ",end=" ")
    print()
    
    
