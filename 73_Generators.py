"""
Iterable - __iter__() or __getitem__()
Iterator - __next__()
Iteration -
"""
# &&&&&&&#####$$$$$$$$$$$ Generator $$$$$$$$$$$$$$$$
# def Gen(n):
# 	for i in range(n):
# 		yield i

# g= Gen(3)

# print(g.__next__())
# print(g.__next__())
# print(g.__next__())
# print(g.__next__())

# for i in g:
# 	print(i)



# m = "12343"
# ier = iter(m)
# print(ier.__next__())
# print(ier.__next__())
# print(ier.__next__())
# print(ier.__next__())
# print(ier.__next__())

# m = "12343"
# ier = iter(m)
# for item in m:
# 	print(item)


# def simple():  
# 	for i in range(10):  
# 			if(i%2==0):  

# 					yield i  
# #Successive Function call using for loop  
# for i in simple():  
#     print(i)  


##############$$$$$$$$$$$$$$$$$$$$$$$ Multiple Yield %%%$$$$$$&&&&&##
# def multiple_yield():  
# 	str1 = "First String"  
# 	yield str1  

# 	str2 = "Second string"  
# 	yield str2  

# 	str3 = "Third String"  
# 	yield str3  

# obj = multiple_yield()  
# print(obj.__next__())
# print(obj.__next__())
# print(obj.__next__())
# print(next(obj))
# print(next(obj))  
# print(next(obj))  



#@@@@@@@@&&&&&&&&&&&&&%%%%%%%%% Generator Expression %%%%%%%%%%%%%%%%%$$$$$$$$$$$###

# We can easily create a generator expression without using user-defined function.
#  It is the same as the lambda function which creates an anonymous function; the generator's
#   expressions create an anonymous generator function.

# The representation of generator expression is similar to the Python list comprehension.
# The only difference is that square bracket is replaced by round parentheses. 
#  The list comprehension calculates the entire list, whereas the generator expression calculates
#   one item at a time.

# list1 = [1,2,3,2,3,3,3,4,4,4]

# # List comprehension
# lc = [i*3 for i in list1]

# # Generator expression

# gc = (i**3 for i in list1)

# print(gc)
# print(lc)

# In the above program, list comprehension has returned the list of
#  cube of elements whereas generator expression has returned the reference
#   of calculated value. Instead of applying a for loop, we can also call next() 
# 	on the generator object. Let's consider another example:


list = [1,2,3,4,5,6]  
  
z = (x**3 for x in list)  
  
print(next(z))  
  
print(next(z))  
  
print(next(z))  
  
print(next(z))  

# def table(n):  
#     for i in range(1,11):  
#         yield n*i  

# tab = table(15)
# for i in tab:
#   print(i)  

# def fibbonacci(n):
# 	a = -1
# 	b = 1
# 	for i in range(1,n+1):
# 		fibb = a + b
# 		a = b
# 		b = fibb
# 		yield fibb

# fibb1 = fibbonacci(5)
# print(fibb1)
# for f in fibb1:
# 	print(f)


# for i in range(2,11):
# 	for j in range(1,11):
# 		print("%dX%d = %d\n"%(i,j,i*j))
		
		


# import sys  

# # List comprehension  
# nums_squared_list = [i * 2 for i in range(1000)]

# print(sys.getsizeof("Memory in Bytes:",nums_squared_list))  

# # Generator Expression  
# nums_squared_gc = (i ** 2 for i in range(1000))  

# print(sys.getsizeof("Memory in Bytes:", nums_squared_gc))
# 


# def x(values):
# 	values[0] = 33
# 	print(values)
# v = [1,2,3]
# x(v)
# # print(v)
