# There can be some functionality that relates to the class, 
# but does not require any instance(s) to do some work, static 
# methods can be used in such cases. A static method is a method
# which is bound to the class and not the object of the class.
# It can’t access or modify class state. It is present in a class
# because it makes sense for the method to be present in class. 
# A static method does not receive an implicit first argument.

from datetime import date
class Person:  
    def __init__(self, name, age):  
        self.name = name  
        self.age = age  
        
    # a static method to check if a Person is adult or not.  
    @staticmethod
    def isAdult(age):   ###&&&&@@@@@-----Static method-------@@@@$$$$$
        if age == 16:
            print("Welcome")
        else:
            print("GO and fuck from here ")
        return 0

    def ageverifier(self):      ##@@@@@$$$------Simple method------@@@@@@@@@@@@@@$$$
        if self.age == 65:
            print("BSDK")
        else:
            print("Accha bsdk")

    @classmethod                           ###&&&&@@@@@-----class method-------@@@@$$$$$
    def fromBirthYear(cls, name, year): 
        cls(name, date.today().year - year) 
        print(f"My name is = {name} And my age is = {year}")
         


per = Person("Mohit",64)
per.ageverifier()
year = Person.fromBirthYear("Mohit",2001)



# from datetime import date
# class Person: 
#     def __init__(self, name, age): 
#         self.name = name 
#         self.age = age 
      
#     # a class method to create a Person object by birth year. 
#     @classmethod
#     def fromBirthYear(cls, name, year): 
#         return cls(name, date.today().year - year) 
      
#     # a static method to check if a Person is adult or not. 
#     @staticmethod
#     def isAdult(age): 
#         return age > 18
  
# person1 = Person('mayank', 21) 
# person2 = Person.fromBirthYear('mayank', 2001) 
  
# print (person1.age) 
# print (person2.age )
  
# # print the result 
print (Person.isAdult(22)) 



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
        return cls(*string.split("-"))
    
    @staticmethod
    def PrintGood(string):
        print("This is a good boy"+string)


harry = Employee("Harry", 255, "Instructor")
rohan = Employee("Rohan", 455, "Student")
karan = Employee.from_dash("Karan-480-Student")    
print(karan.salary)
