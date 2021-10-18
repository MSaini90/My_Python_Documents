# # == - value equality - Two objects have the same value 
# # is - reference equality - Two referces refer to the same object

# a = [2,2,3,4]
# b = a
# print(b == a)
# print(b is a)

# b[0] = 0
# print(a)
# print(b)

# c = a[:]  #New copy of "a"
# print(b == c)
# print(a == c)

# print(c is a) 
# print(c is b)


a = [6, 4, "34"]
b = [6, 4, "34"]
print(b is a )
