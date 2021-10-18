"""
def fact(n):
	fac=1
	for i in range(n):
		fac=fac*(i+1)
	return(fac)

num=int(input("Enter number for factorial="))
print(fact(num))"""
"""
def fact(n):
	if n==1:
		return 1
	else:
		return(n*fact(n-1)) 
num=int(input("Enter number for factorial="))
print(fact(num))"""


"""		
a=-1 
b=1
n=int(input("Enter nth term"))
for i in range(0,n):
	c=a+b
	a=b
	b=c
	print(c)
"""
def Fibbonacci(n):
	a=0
	b=1
	for i in range(1,n+1):
		c=a+b
		a=b
		b=c
		print(c)
	
num=int(input("Enter number"))
Fibbonacci(num)

			

    

