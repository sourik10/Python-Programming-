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



