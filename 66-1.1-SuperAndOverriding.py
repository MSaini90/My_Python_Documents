"""
class A:
    classvar1 = "I am a class variable in class A"
    def __init__(self):
        self.var1 = "I am inside class A's constructor"
        self.classvar1 = "Instance var in class A"
        self.special="Special"
        self.txt="HEllo"

    def PrintTEXT(self):
      print(self.txt)
    
class B(A):
  classvar1 = "I am in class B"
  def __init__(self):

    # super().__init__()
    self.var1 = "I am inside class B's constructor"
    self.classvar1 = "Instance var in class B"
    super().__init__()
    print(super().classvar1)
    # print(super().PrintTEXT())
    

a = A()
b=B()
print(b.special,"\n",b.classvar1,"\n",b.var1)
"""
"""
class Parent:
  def __init__(self,txt):
    self.message=txt
  
  def printMessage(self):
    print(self.message)

class Child(Parent):
  def __init__(self,txt):
    super().__init__(txt)

par=Child("Hello my name is Mohit Saini")
par.printMessage()

    
"""
"""
class parent:
  def __init__(self):
    self.value="parent class version"

  def printvalue(self):
    print(self.value)

class child(parent):
  def __init__(self):
    self.value="Child class version"
 
  def printvalue(self):
    print(self.value)

par=parent()
chi=child()
par.printvalue()
chi.printvalue()
"""

"""
class parent1:
  def show(self):
    print("This is a version of parent1's class")

class parent2:
  def display(self):
    print("This is a version of parent2's class")

class Child(parent1,parent2):
  def show(self):
    print("This is a version of Chid class")

# parent=parent1()
# parent.show()

chid=Child()
chid.show()
chid.display()
"""


# using by class name with in overriden method
"""
class Parent(): 
    def show(self): 
        print("Inside Parent") 
          
class Child(Parent): 
    def show(self): 
      # Calling the parent's class 
      # method 
      Parent.show(self) 
      # super().show() #using super method
      print("Inside Child") 
        
# Driver's code 
obj = Child() 
obj.show()
"""



"""
class America:
  def __init__(self):
    print("Hi i am presidents of America and my name is 'Donald Trump' And my best friend 'Covind'")
  def Salary(self,salry):
    print(f"My salary is {salry} dolar")

class India:
  def __init__(self):
    print("Hi i am presidents of India and my name is 'Ramnath Covind' and my girlfreind Angela So sexy")
    super().__init__()

  def Salary(self,salry):
    print(f"My salary is {salry} dolar")
    super().Salary(salry+100)

class Germany:
  def __init__(self):
    print("Hi i am presidents of Germany and my name is 'Angela Markel'")
    super().__init__()

  def Salary(self,salry):
    print(f"My salary is {salry} dolar")
    super().Salary(salry+200)

germ=Germany()
germ.Salary(200000)
"""

"""
  
class GFG1:  
    def __init__(self):  
        print('HEY !!!!!! GfG I am initialised(Class GEG1)')  
    
    def sub_GFG(self, b):  
        print('Printing from class GFG1:', b)  
    

class GFG2(GFG1):  
    def __init__(self):  
        print('HEY !!!!!! GfG I am initialised(Class GEG2)')  
        super().__init__()  
    
    def sub_GFG(self, b):  
        print('Printing from class GFG2:', b)  
        super().sub_GFG(b + 1)  
    
# class GFG3 inherits the GFG1 ang GFG2 both  
class GFG3(GFG2):  
    def __init__(self):  
        print('HEY !!!!!! GfG I am initialised(Class GEG3)')  
        super().__init__()  
    
    def sub_GFG(self, b):  
        print('Printing from class GFG3:', b)  
        super().sub_GFG(b + 1)  
    
    
# main function  
if __name__ == '__main__':  
    
    # created the object gfg  
    gfg = GFG3()  
    
    # calling the function sub_GFG3() from class GHG3  
    # which inherits both GFG1 and GFG2 classes  
    gfg.sub_GFG(10) """