#file-handling in Python

a=open("file.txt","r")  #opening file.txt file in read mode

b=a.read()              #reading all content
print(b)

#c=a.read(10)    
#print(c)                #printing content in file.txt



#d=a.readline()        #reading first line in file.txt
#print(d)  

a.close()               #closing file.txt




#no need to write f.close() while using 'with' statement
'''
with open(“this.txt”) as f:

            f.read()
            
'''



