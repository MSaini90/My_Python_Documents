
# In the below example we use a staticmethod() and classmethod() 
# to check if a person is an adult or not.


# Python program to demonstrate  
# use of a class method and static method. 
# from datetime import date 
  
# class Person: 
#     def __init__(self, name, age): 
#         self.name = name 
#         self.age = age 
      
#     # a class method to create a  
#     # Person object by birth year. 
#     @classmethod
#     def fromBirthYear(cls, name, year): 
#         return cls(name, date.today().year - year) 
      
#     # a static method to check if a 
#     # Person is adult or not. 
#     @staticmethod
#     def isAdult(age): 
#         return age > 18
  
# person1 = Person('mayank', 21) 
# person2 = Person.fromBirthYear('mayank', 1996) 
  
# print (person1.age) 
# print (person2.age) 
  
# # print the result 
# print (Person.isAdult(22)) 

# # Output:
# 21
# 22
# True



class Employee:
	no_of_employee=8
	
	def __init__(self,name,salary,roll_no):
		self.name=name
		self.salary=salary
		self.rollno=roll_no
	
	def PrintDetails(self):
	  return(f"The name is {self.name}. Salary is {self.salary} and roll is {self.rollno}")


	# @classmethod
	# def change_leaves(cls,newleaves):

    #    cls.no_of_employee=newleaves


	@classmethod
	def from_dash(cls,string):
	  params=string.split("-")
    #   print(params)
	  return cls(params[0],params[1],params[2])
      
      

Mohit=Employee("Mohit",1800000,1804049)
Mohit.PrintDetails()
print(Mohit.rollno)
# Mohit.change_leaves(47)

karan = Employee.from_dash("Karan-480-Student")
print(karan.name)








#==--------------------------------In one line=-------------------------# 
"""
class Employee:
    no_of_leaves = 8

    def __init__(self, aname, asalary, arole):
        self.name = aname
        self.salary = asalary
        self.role = arole

    def printdetails(self):
        return f"The Name is {self.name}. Salary is {self.salary} and role is {self.role}"

    @classmethod
    def change_leaves(cls, newleaves):
        cls.no_of_leaves = newleaves

    @classmethod
    def from_dash(cls, string):

        #  params = string.split("-")
        # #  print(params)
        #  return cls(params[0], params[1], params[2])
        return cls(*string.split("-"))


harry = Employee("Harry", 255, "Instructor")
rohan = Employee("Rohan", 455, "Student")
karan = Employee.from_dash("Karan-480-Student")

print(karan.salary)

"""