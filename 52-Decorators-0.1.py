
# def printname(age):
# 	def name():
# 		fname = input("Enter first name=")
# 		Sname = input("Enter second name=")
# 		age()
# 		print("Your name is = "+fname , Sname)
# 	return name

# @printname
# def age():
# 	age = int(input("Enter your age ="))	
# 	print("\nYour age is = ",age)

# age()


# def mohit():
# 	x = 20
# 	def saini():
# 		global x
# 		x = 88
# 	print("Before calling saini()", x)
# 	saini()
# 	print("After calling saini()",x)
	
# mohit()
# print(x)

# cook your dish here
x,y = map(float,input().split())
if int(x)%5==0 and x<=y-0.5:
    print("%.2f"%(y-x-0.5))
else:
    # a = "%.2f"%y
    print("%.2f"%y)