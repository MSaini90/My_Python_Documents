# join()

# Join all items in a tuple into a 
# string,using a hash character as
# separator:

# myTuple = ("John", "Peter", "Vicky")
# x = "#".join(myTuple)
# print(x)

# The join() method takes all items 
# in an iterable and joins them into
# one string.

# A string must be specified as the
# separator.

# Syntax
# string.join(iterable)

dic =  {'key1': 1, 'key2': 2}  
str = ' & '  
str = str.join(dic)    
print(str)  

# myDict = {"name": "John", "country": "Norway"}
# mySeparator = "TEST"
# x = mySeparator.join(myDict)
# print(x)

# Note: When using a dictionary as an iterable, the 
# returned values are the keys, not the values.



# lst=["Romen reigns","John sinha","Undertaker","Yogeshwar datt"]
# for item in lst:
# 	print(item," and " , end="")

# a=" and ".join(lst)
# print(a,"Others WWE SUperstars")

