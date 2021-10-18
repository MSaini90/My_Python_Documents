# a=57
# b=45
# c=sum((a,b))
# print(c)


"""def printme(name,age=22):    
    print("My name is",name,"and age is",age)    
printme(name = "john",age=45)     
printme(age = 10,name="David") """

"""
def printme(*names):    
  print("type of passed argument is ",type(names))    
  print("printing the passed arguments...")    
  for name in names:    
    print(name)    
printme("john","David","smith","nick")    """


"""
def printme(name,age):
	print(f"Hello my name is {name} and my age {age}")
printme(name="Mohit Saini",agew=53)"""

def printme(**kwargs):
	print(f"All name is {kwargs}")
printme(name="Mohit",name2="Saini")
"""
def food(**kwargs):  
		print(kwargs)  
food(a="Apple")  
food(fruits="Orange", Vagitables="Carrot")  """


def function(a,b):
  """This function calculate average of two numbers """  #<---docstring
  average=(a+b)/2
  return average
print(function.__doc__)
f=function(2,5)
print(f)