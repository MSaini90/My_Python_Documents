
# class calculation1:
# 	def mul(self,num1,num2):
# 		return num1*num2
# class calculation2:
# 	def add(self,num1,num2):
# 		return num1+num2
# class calculation3:
# 	def sub(self,num1,num2):
# 		return num1-num2
# class derived(calculation1,calculation2,calculation3):
# 	def derived(self,num1,num2):
# 		return num1/num2

# num1=int(input("Enter number one="))

# num2=int(input("Enter nunber two="))
# div=derived()
# mul=div.mul(num1,num2)
# add=div.add(num1,num2)
# sub=div.sub(num1,num2)

# div=div.derived(num1,num2)
# print(mul)
# print(add)
# print(sub)
# print(div)




class Employee:
    no_of_leaves = 8
    # var=68
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


class Player:
		var=6767
	
		no_of_games = 4
	
		def __init__(self, name, game):
				self.name = name
				self.game =game
	
		def Printdetails(self):	
				return f"The name is {self.name} and game is {self.game}"

# shubham = Player("Shubham", ["Cricket"])
				
class CoolProgrammer(Employee,Player):
	# var = 10
	language="Python"
	def PrintLanguage(self):
		print(self.language)

harry = Employee("Harry", 255, "Instructor")
rohan = Employee("Rohan", 455, "Student")
saini= Player("Shubham", ["Cricket"])
# print(saini.Printdetails())


karan=CoolProgrammer("Karan","9000","CoolProgrammer")
det = karan.printdetails()
print(det)
# Player=karan.Printdetails()
# print(Player)
# karan.PrintLanguage()
print(karan.var) 


