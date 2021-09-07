#Write a program to find the sum of first n natural numbers using a while loop.
n=int(input("enter n: "))
s=0
while(n):
    s=s+n
    n=n-1
print(s)
