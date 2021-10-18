"""class Animal:

	def speak(self):
		m=input("Enter the cat voice=")
		print("The cat is",m)
class Dog(Animal):
	def bark(self,bark):
		print("The dog is ",bark)

dg=Dog()
dg.bark("Barking")
dg.speak()
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
        return cls(*string.split("-"))
    
    @staticmethod
    def PrintGood(string):
        print("This is a good boy"+string)


harry = Employee("Harry", 255, "Instructor")
rohan = Employee("Rohan", 455, "Student")
karan = Employee.from_dash("Karan-480-Student")    
# print(karan.salary)

class Programmer(Employee):
    def __init__(self, aname, asalary, arole,languages):
        self.name = aname
        self.salary = asalary
        self.role = arole
        self.language=languages


    def PrintProgrammer(self):
        return f"The Programmer's name is {self.name}. Salary is {self.salary} and role is {self.role} and languages are {self.language}"     

        

karan = Programmer("Karan",5656,"programmer",["Python","java","Php"])             

print(karan.PrintProgrammer())
