#oops----object oriented programming
#class,object methods

class student:  #class name student 

    subject="physics"   #class attributes (subject,h_marks)
    h_marks=100
    
    #methods create
    def f1(self):
        print("xyz is a good student")
        
    #not using 'self' keyword in methods
    @staticmethod
    def f2():
        print("messi is the boss")
        
    #constructor---no argument,no return type
    def __init__(self):
        print("constructor created")
    
        
        
    
    
#object instantiation
sourik=student()
student.h_marks=95      #changing class attributes to instance attributes 
print(sourik.h_marks)
sourik.f1() 
sourik.f2()

#adding instance attributes
sourik.roll=80
print(sourik.roll)




