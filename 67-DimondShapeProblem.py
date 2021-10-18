class A:
	def met(self):
		print("This met method is class A")
class B(A):
	def met(self):
		print("This met method is class B")
class C(A):
	def met(self):
		print("This met method is class C")
class D(C,B):
	pass


a=A()
b=B()
c=C()
d=D()

print(d.met())