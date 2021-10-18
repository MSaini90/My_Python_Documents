#****************@@@@@@@@@####### --map function--  #########@@@@@@@@@**************#
"""
Python map() Function
The python map() function is used to return a list of results after applying a given function to each item of an iterable(list, tuple etc.)

Signature
map(function, iterables)  
Parameters
function- It is a function in which a map passes each item of the iterable.

iterables- It is a sequence, collection or an iterator object which is to be mapped.
"""


"""numbers=["22","43","56"]
for i in (range(len(numbers))):j
	numbers[i]=int(numbers[i])
numbers[2]=numbers[2]+1
print(numbers[2]) """


"""
numbers=["22","43","56"]
numbers=list(map(int,numbers))
numbers[2]=numbers[2]+1
print(numbers[2])
"""


# def sq(a):
# 	return a*a
# num = [3,4,5,6]
# for i in num:
# 	n=sq(i)
# 	print(n)


# def sq(a):
# 	return a*a
# num=(3,4,5,6,3,2,,9)
# square=list(map(sq,num))
# print(square)



# num=[2,3,4,5,6,]
# square=list(map(lambda x: x*x,num))
# print(square)



# def square(a):
# 	return(a*a)
# def cube(a):
# 	return(a*a*a)
# func=[square,cube]
# for i in range(5):
# 	val= list(map(lambda x:x(i),func))   #def val(x,i): for i in range(5): return(x*i)
# 	print(val)

	
	
	#****************@@@@@@@@@####### --Filter function--  #########@@@@@@@@@**************#


# Python filter() function is used to get filtered elements.
# This function takes two arguments, 
# first is a function and the second is iterable.
# The filter function returns a sequence from those 
# elements of iterable for which function returns True.
# The first argument can be None if the function is
# not available and returns only elements that are True.

# Signature
# filter (function, iterable)  

#                      Parameters
# 										     |
# (1)-function: It is a function. If set to None returns only elements that are True.
# (2)-Iterable: Any iterable sequence like list, tuple, and string.
# Both the parameters are required.

# Return
# It returns the same as returned by the function.



# def is_greater_5(num):
# 	if(num>5):
# 		return num
# number=[3,4,5,6,3,7,44,44,]
# for item in number:
# 	gn = is_greater_5(item)
# 	print(gn)

lst = (10,22,37,41,100,123,29)  
oddlist = tuple(filter(lambda x:(x%2== 0),lst)) 
print(oddlist)    

# lst=[3,7,6,3,2,2,9,20]
# def is_greater_5(num):
# 	if(num>5):
# 		print("Numbers")
# greater_than5=list(filter(is_greater_5,lst))



#****************@@@@@@@@@####### --reduce function--  #########@@@@@@@@@**************#
# lst=[5,4,3,3]
# sum=0
# for i in lst:
	# sum=sum+i
# print(sum)


# from functools import reduce
# lst=[3,4,5,6,7]
# prod=reduce(lambda x,y:x+y,lst)
# print(prod)