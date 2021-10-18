# a = A class method is a method which is bound to the class and not the object of the class.
# b = They have the access to the state of the class as it takes a class parameter that points 
# c = to the class and not the object instance.
# d = It can modify a class state that would apply across all the instances of the class.
#  For example, it can modify a class variable that would be applicable to all the instances.





# class Employee:
# 	no_of_leaves=8
# 	def __init__(self,name,salary,roll_no):
# 		self.name=name
# 		self.salary=salary
# 		self.rollno=roll_no

# 	def PrintDetails(self):
# 	  return(f"The name is {self.name}. Salary is {self.salary} and roll is {self.rollno}")

# 	@classmethod
# 	def Change_Leaves(cls,newleaves):
# 		cls.no_of_leaves=newleaves

	
# Mohit=Employee("Mohit",1800000,1804049)
# Mohit.Change_Leaves(54)
# print(Mohit.no_of_leaves)



# class Student:
# 	name="Geekys"

# 	def print_name(obj):
# 		print(f"The name is:",obj.name) 

# Student.print_name=classmethod(Student.print_name)

# print(Student.print_name)

# Student.print_name()



# Python program to demonstrate  
# use of a class method and static method. 
from datetime import date  
class Person: 
    def __init__(self, name, age): 
        self.name = name 
        self.age = age 
      
    # a class method to create a  
    # Person object by birth year. 
    @classmethod
    def fromBirthYear(cls, name, year): 
        return cls(name, date.today().year - year) 
      
    # a static method to check if a 
    # Person is adult or not. 
    @staticmethod
    def isAdult(age): 
        return age > 18
  
person1 = Person('mayank', 21) 
person2 = Person.fromBirthYear('mayank', 1996) 
  
print (person1.age) 
print (person2.age) 
# print the result 
print (Person.isAdult(22)) 


