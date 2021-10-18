
# def function1():
# 	print("Welcome")
# function2=function1
# del function1
# function2()



# def functionret(num):
# 	if num==0:
# 		return print
# 	if num==1:
# 		return int
# a=functionret(0)
# print(a) 



# def executor(func):
# 	func("This")
# executor(print)





# def func():  
#      print("We are in first function")  
#      def func1():  
#            print("This is first child function")  
#      def func2():  
#            print(" This is second child function")  
#      func1()  
#      func2()  
#func()


# def dec1(func1):
# 	def nowexec():
# 		print("Executing now")
# 		func1()
# 		print("Executed")
# 	return nowexec

# @dec1
# def whoismohit():
# 	print("Mohit is s good ")

# # whoismohit = dec1(whoismohit)
# whoismohit()



# @@@@@@@@@@@@@@@@@############By my sirg@@@@@@@@@@@@

def decor_result(result_function):
	def distinction(marks):
		for m in marks:
			if m>75:
				print("Distinction")
		result_function(marks)
	return distinction

@decor_result
def result(marks):
	for m in marks:
		if m>=33:
			pass
		else:
			print("Fail")
			break
	else:
		print("PASS")

result([54,34,89,90,76])


