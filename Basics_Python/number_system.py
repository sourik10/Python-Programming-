#decimal 2 binary number system
n=int(input("enter decimal no: "))
temp=[]
while(n>0):
    temp.append(n%2)
    n=n//2
binary=temp[ : :-1]
print("binary representation: ")
for i in binary:
    print(i,end="")
    
    
#decimal 2 octal number system    
n=int(input("enter decimal no: "))
temp=[]
while(n>0):
    temp.append(n%8)
    n=n//8
binary=temp[ : :-1]
print("octal representation: ")
for i in binary:
    print(i,end="")
    
    
    
#decimal to hexadecimal
n=int(input())
print(hex(n))




    
    
 
    




    

    

   
    
    
