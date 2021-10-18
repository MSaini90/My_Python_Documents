

class Employee:
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname
        # self.email = f"{fname}.{lname}@codewithharry.com"

    def explain(self):
        return f"This employee is {self.fname} {self.lname}"

    @property
    def email(self):
        if self.fname==None or self.lname == None:
            return "Email is not set. Please set it using setter"
        return f"{self.fname}.{self.lname}@codewithharry.com"

    @email.setter
    def email(self, string):
        print("Setting now...")
        names = string.split("@")[0]
        self.fname = names.split(".")[0]
        self.lname = names.split(".")[1]

    @email.deleter
    def email(self):
        self.fname = None
        self.lname = None


hindustani_supporter = Employee("Hindustani", "Supporter")

print(hindustani_supporter.email)
hindustani_supporter.fname = "US"
print(hindustani_supporter.email)

hindustani_supporter.email = "this.that@codewithharry.com"
print(hindustani_supporter.email)

del hindustani_supporter.email
print(hindustani_supporter.email)
# hindustani_supporter.email = "Harry.Perry@codewithharry.com"
# print(hindustani_supporter.email)



"""
class student:
	def __init__(self,name,grade):
		self.name = name
		self.grade = grade

# 	def msg(self):
# 		return self.name + " Got grade " + self.grade #As a sample

# 	def setter(self,msg):
# 		sent = msg.split(" ")
# 		print(sent)
# 		self.name = sent[0]
# 		self.grade = sent[-1]

# stud = student("Mohit","C")
# stud.setter("MS gor grade E")

# print("Name :",stud.name)
# print("Grade:" ,stud.grade)
# print(stud.msg)


	@property
	def msg(self):
		return self.name + " Got grade " + self.grade

	@msg.setter
	def msg(self,msg):
		sent = msg.split(" ")
		print(sent)
		self.name = sent[0]
		self.grade = sent[-1]

stud = student("Mohit","C")
stud.msg = "MS got grade E"
print("Name :",stud.name)
print("Grade:" ,stud.grade)
# print(stud.msg)@
"""