#Write a program to calculate the factorial of a given number using for loop.


def fact(num):
    if(num==1):
        return 1
    else:
        return num * fact(num-1)
   
n=int(input("enter n: "))
s=fact(n)
print(s)
