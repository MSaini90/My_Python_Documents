

"""
class Employee:
	def __init__(self,fname,lname):
		self.fname=fname
		self.lname=lname
		# self.email=f"{fname}.{lname}@gmail.com"

	def explain(self):
		return f"This employee is {self.fname} {self.lname}"

	@property	
	def printEmail(self):
		return f"{self.fname}.{self.lname}@gmail.com"
  
Mohit=Employee("Mohit","Saini")

# print(Mohit.email)
print(Mohit.printEmail)

Mohit.fname="US"

# print(Mohit.email)
print(Mohit.printEmail)

# Mohit.printEmail="This.@gmail.com"
# """


class student:
	def __init__(self,name,grade):
		self.name = name
		self.grade = grade
		# self.msg = self.name + " got grade "+ self.grade

	@property
	def msg(self):
		return self.name + " Got grade " + self.grade

stud = student("Mohit","B")

stud.grade = "A"
print("Name :",stud.name)
print("Grade:" ,stud.grade)
print(stud.msg)
