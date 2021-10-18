# num=int(input("Enter your number as far as you want to print the star="))
"""
yes=input("Enter yes/no=")
if yes=="yes":
	for i in range(1,5+1):
		for j in range(1,5+1):
			if(j<=i):
					print("*",end="")
			else:
				print("",end="")
		print()"""
# elif yes=="no":
for i in range(1,6):
	for j in range(1,6):
		if j>=6-i:
			print("*",end='')
		else:
			print("",end='')
	print()
