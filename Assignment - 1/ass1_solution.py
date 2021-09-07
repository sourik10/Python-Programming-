#1. Given a string of length greater than 2, return a string except 1st and last characters
s=input("enter string: ")
print(s[1:-1])




#2. Given 2 strings, s1, and s2 return a new string made of the first, middle and last char each input string.

s1=input("enter first string: ")
s2=input("enter second string: ")
first=s1[:1]+s2[:1]
last=s1[len(s1)-1]+s2[len(s2)-1]
middle=s1[len(s1):len(s1)+1] + s2[len(s2):len(s2)+1]

res=first+middle+last
print(res)



#3. Given 2 strings, s1 and s2, create a new string by appending s2 in the middle of s1

s1=input("enter first string: ")
s2=input("enter second string: ")
m=len(s1)

print(s1[0:int(m/2)] + s2 + s1[int(m/2):])



#4. Find all occurrences of “India” in given string ignoring the case.
str=input ("Enter the string: ")
tempString = str.lower()
print(tempString.count('india'))


#5.Find the last position of a substring “Emma” in a given string
str1 = "Emma is a data scientist who knows Python. Emma works at google."
index = str1.rfind("Emma")
print(index)


#6. Display the two substring separated by space.
s=input("enter the string: ")
a=s[ :int(len(s)/2)]
b=s[int(len(s)/2): ]
print(a," ",b)


#8. Reverse the following tuple aTuple = (10, 20, 30, 40, 50)
aTuple = (10, 20, 30, 40, 50)
n=aTuple[: :-1]
print(n)


#9.Access value 20 from the following tuple aTuple = ("Orange", [10, 20, 30], (5, 15,25))
aTuple = ("Orange", [10, 20, 30], (5, 15,25))
print(aTuple[1][1])



#10. Unpack the following tuple into 4 variables aTuple = (10, 20, 30, 40)
aTuple = (10, 20, 30, 40)
for i in aTuple:
    print(i)
    
    
#11.Swap the following two tuples tuple1 = (11, 22) tuple2 = (99, 88)
tuple1 = (11, 22) 
tuple2 = (99, 88)

temp=tuple1
tuple1=tuple2
tuple2=temp

print(tuple1)
print(tuple2)


#12.Copy element 44 and 55 from the following tuple into a new tuple  tuple1 = (11, 22,33, 44, 55, 66)
tuple1 = (11, 22,33, 44, 55, 66)

t=tuple1[3:5]
print(t)



#13.Modify the first item (22) of a list inside a following tuple to 222 tuple1 = (11, [22,33], 44, 55)
tuple1 = (11, [22,33], 44, 55)
tuple1[1][0]=222
print(tuple1)



#15.Merge following two Python dictionaries into one dict1
#dict1 = {'Ten': 10, 'Twenty': 20, 'Thirty': 30}
#dict2 = {'Thirty': 30, 'Fourty': 40, 'Fifty': 50}


dict1 = {'Ten': 10, 'Twenty': 20, 'Thirty': 30}
dict2 = {'Thirty': 30, 'Fourty': 40, 'Fifty': 50}

dict3=dict1.copy()
dict3.update(dict2)

print(dict3)


#16.








