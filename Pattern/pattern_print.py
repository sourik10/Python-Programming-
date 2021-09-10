 #1: Simple Number Triangle Pattern
r=int(input())
num=1;
for i in range(0,r):
    for j in range(0,i+1):
        print(num,end="")
    print(" ")
    num=num+1
    
    

#2: Inverted Pyramid of Numbers
r=int(input())
num=r;
for i in range(r,0,-1):
    for j in range(0,i):
        print(num,end="")
    print(" ")
    num=num-1
    

   
 #6: Reverse Pyramid of Numbers
r=int(input())
for i in range(0,r):
    for j in range(i,0,-1):
        print(j,end=(''))
    print(" ")


    
#7: Inverted Half Pyramid Number Pattern
r=int(input())
for i in range(r,0,-1):
    for j in range(0,i+1):
        print(j,end=(''))
    print(" ")

        

        
