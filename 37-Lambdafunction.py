#Lambda functions or anonymous functions
# Syntax
# lambda arguments : expression


# x=lambda a:a*10
# num=int(input("Enter number="))
# print("Multiplication is=",x(num))


x = lambda a:a+10   
# Here we are printing the function object  
print(x)  
print("sum = ",x(20)) 


# def a_first(a):
# 	return a[0]

# a = [[288,3] , [64,4] , [4,5]]
# a.sort(key = a_first)
# print(a)

# a=[[12,99],[3,5],[6,7]]
# a.sort(key=lambda X:X[1])
# print(a)