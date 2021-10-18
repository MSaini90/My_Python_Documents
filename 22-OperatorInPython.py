# Comparison Operator
# i=4
# print(i<5)
# a=True
# b=False

# Identity operator
a=True
b=True
# print(4 is 5)

lst=[]
print("How many names you want to enter")
i=int(input())
print("Enter names")
Index=1
for k in range(0,i):
	print(Index,end="=")
	n=input()
	lst.append(n)
	Index=Index+1
print("Successfully Entered")
# print(lst)
print("Will you check name is present or not in the list Enter 1-for yes 0-for no")
check=int(input())
if check==1:
	name=input("Enter your name for checking=")
	tr=name in lst
	if tr==True:
		print("Congratulate your name is present in the list\n")
		print("***",name,"***\n")
	else:
		print("Sorry! Your data is not present in the list")

else:
	print("Ok as your wish")