# If we write the statement:
# If-expression if(Condition) else else-expression

# It will be same as:
# if condition:
#    if-expression
# else:
#    else-expression

a = int(input("enter a\n"))
b = int(input("enter b\n"))

# if a>b: print("A B se bada hai bhai")
print("B A se bada hai bhai") if a<b else print("A B se badha hain")