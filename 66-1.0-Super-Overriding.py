
class A:
	# classvar1="I am a class variable in class A"
	def __init__(self):
		self.var1="I am inside class A's constructor"
		self.classvar1="I am Instance  Variable in class A"
		self.special = "Special"

class B(A):
	classvar1="I am a class variable in class B"
	def __init__(self):
		# super().__init__()
		super(B, self).__init__ ()
		self.var1="I am inside class B's constructor"
		self.classvar1="I am Instance  Variable in class B"
		print(super().classvar1)    

a=A()
b=B()

print(b.special)
print( b.var1 )
print(b.classvar1)
