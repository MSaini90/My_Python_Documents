"""class Geek:

  def __init__(self,name,age):
      self.name=name
      self.age=age

  def ShowAge(self):
   		print(f"The age is {self.age} and name is {self.name}")

obj = Geek("R2J", 20)
# # calling public member function of the class  
obj.ShowAge()
# # accessing public data member 
print(f"The age is {obj.name} and name is {obj.age}")
		"""
  


#Super class 
class Gekks:
	_name=None
	_roll_nO=None
	_branch=None

	def __init__(self,name,roll,branch):
		self._name=name
		self._roll_nO=roll
		self._branch=branch
	
	def DisplayRollAndBranch(self):
		print(f"The roll no is {self._roll_nO} and name is {self._name}")

#Derived class
class geeks(Gekks):
  # constructor  
  def __init__(self, name, roll, branch):
			Gekks.__init__(self, name, roll, branch)     
       # public member function  
  def displayDetails(self): 
		# accessing protected data members of super class  
    print("Name: ", self._name)  
    # accessing protected member functions of super class  
    self.DisplayRollAndBranch() 
  
# creating objects of the derived class         
obj = geeks("Mohit Saini", 1706256, "Information Technology")  
# calling public member functions of the class 
obj.displayDetails()