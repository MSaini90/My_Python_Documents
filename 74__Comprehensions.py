# ls = []
# i = 0
# for i in range(100):
# 	if i%3==0:
# 		i = i+1
# 		ls.append(i)
# print(ls)
# print("Total element in the list which is divisible be 3")
# print(i)


#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@ List comprehensions &&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&
# Syntax : newList = [ expression(element) for element in oldList if condition ]

# ls=[i for i in range (10) if i%3==0]
# print(ls)


#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@ Dictionary comprehensions &&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&
# Syntax : {key: value for (key, value) in iterable if condition}
# dict1={ i:f"item {i}" for i in range(1,10) if i%2==0 } #Dictionary comprehensions
# print(dict1)  

# dict1={ i:f"item {i}" for i in range(5) }
# dict2={ value:key for key,value in dict1.items() }
# print(dict1)
# print(dict2)
# print(dict1,"\n",dict2)

# square_dict = dict()
# for num in range(1, 11):
#     square_dict[num] = num*num
# print(square_dict)


# @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@ Set comprehensions &&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&
# dresses= {dress for dress in ["dress1","dress2","dress1",  
#                                  "dress2","dress1","dress2","dress3"]}
# print(type(dresses))
# print(dresses)



#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@ Generator comprehensions &&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&
evens=(i for i in range(100) if i%2==0)
print(type(evens))
# print(evens.__next__())
# print(evens.__next__())
# print(evens.__next__())
for i in evens:
	print(i)
	
