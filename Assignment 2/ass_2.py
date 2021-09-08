#1.Write a Python Program to Find the Smallest Divisor of an Integer other than 1

n=int(input("enter number: "))
for i in range (2,n+1):
    if(n%i==0):
        print(i)
        break
    
if(i==n):
    print("no divisor other than 1")
    
    

    
#2.Write a Python Program to Check whether a Number is a Palindrome or not.

n=int(input("Enter any number: "))
temp=n
sum=0

while (n>0):
    rem=n%10
    sum=(sum*10)+rem;
    n=n//10
    
if (temp==sum):
    print("Palindrome.")
else:
    print ("Not a palindrome.")
    
    
    
    
        
