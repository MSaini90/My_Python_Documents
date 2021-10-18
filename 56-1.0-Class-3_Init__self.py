
# What is the use of Self in Python?

# The self is used to represent the instance of the class.
#  With this keyword, you can access the attributes and
#   methods of the class in python. It binds the attributes 
# 	with the given arguments. The reason why we use self is 
# 	that Python does not use the ‘@’ syntax to refer to instance attributes.
# 	 In Python, we have methods that make the instance to be passed 
# 	 automatically, but not received automatically.


# class Employee:
# 	NoOfLives=5
# 	def PrintDetails(self):
# 	  print(f"The name is {self.name}. Salary is {self.salary} and roll is {self.role}")

# Mohit=Employee()
# Rohan=Employee()

# Mohit.salary=45000
# Mohit.role="Techmakny"
# Mohit.name="Mohit"

# Rohan.salary=4500
# Rohan.role="1808065"
# Rohan.name="Rohan"
# print(Rohan.PrintDetails())

# class student:
	
#   age = int(input("Enter student age="))
#   def studentInfo(self):
# 			print("Age is =",self.age)

# std = student()
# std.studentInfo()




"""
class Employee:
	def Display(self,id,name):
		print(f"The id is {id} and name is {name}")
id1=int(input("Enter id"))
name=input("Enter name")
emp=Employee()
emp.Display(id1,name)

print(emp.__doc__)
print(emp.__dict__)
"""

"""
class Employee:
	def PrintDetails(self,nm,sl,rl):
		print(f"The name is {nm}. Salary is {sl} and roll is {rl}")

name=input("Enter employee name=")
salary=input("Enter employee salary=")
roll_no=input("Enter employee roll no=")
Mohit=Employee()
Mohit.PrintDetails(name,salary,roll_no)
"""




"""
class Employee:
	def PrintDetails(self,num1,num2,num3):
		mul=num1*num2*num3
		
		print(f"The multiplication is={mul} ")

num1=int(input("Enter number1="))
num2=int(input("Enter number2="))
num3=int(input("Enter number3="))
Mohit=Employee()
Mohit.PrintDetails(num1,num2,num3)
"""



# Concept of Constructor

# class Employee:
# 	def __init__(self,name,salary,roll_no):
# 		self.name=name
# 		self.salary=salary
# 		self.rollno=roll_no
# 	def PrintDetails(self):
# 	  print(f"The name is {self.name}. Salary is {self.salary} and roll is {self.rollno}")
# Mohit=Employee("Mohit",1800000,1804049)
# Mohit.PrintDetails()
# print(Mohit.salary)


# class Employee:

# 	def __init__(self,name,salary,roll_no):
# 		print(f"The name is {name}. Salary is {salary} and roll is {roll_no}")
   
# Mohit=Employee("Mohit",1800000,1804049)



# class Employee:
#  	def __init__(self,name,id):
# 		 self.i=id
# 		 self.nm=name
	
	
# 	def Display(self):
												
# 		print(f"The name is {self.nm} and id {self.i}")


# Emp=Employee("Mohit",1)
# Emp.Display()

"""
# Non parameterized constructor
class Student:
	def __init__(self):
		print("Hello Programmer i am non-parameterized constructor")
	def Hllo(self,name):
	  print("Hi",name)
St=Student()
St.Hllo("Mohit")
	"""

# Parameterized constructor
# class Employee:
# 	def __init__(self,name):
# 		print("This is parameterized constructor")
# 		self.name=name
# 	def Display(self):
# 		print(f"Hii {self.name} ")
# emp=Employee("Mohit")
# emp.Display()


# class Student:  
#     roll_num = 101  
#     name = "Joseph"  
  
#     def display(self):  
#         print(self.roll_num,self.name)  
  
# st = Student()  
# st.display()  

"""
class Student:  
    def __init__(self, name, id, age):  
        self.name = name  
        self.id = id  
        self.age = age  
  
    # creates the object of the class Student  
s = Student("John", 101, 22)  
  
# prints the attribute name of the object s  
print(getattr(s, 'name'))  
  
# reset the value of attribute age to 23  
setattr(s, "age", 23)  
  
# prints the modified value of age  
print(getattr(s, 'age'))  
  
# prints true if the student contains the attribute with name id  
  
print(hasattr(s, 'id'))  
# deletes the attribute age  
delattr(s, 'age')  
  
# this will give an error since the attribute age has been deleted  
print(s.age)"""