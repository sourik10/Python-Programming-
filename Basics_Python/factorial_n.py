#Write a program to calculate the factorial of a given number using for loop.

n=int(input("enter n: "))
s=1
while(n):
    s=s*n
    n=n-1
print(s)
