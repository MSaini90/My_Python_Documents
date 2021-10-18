import os
lst=[]
# num=int(input("How many people's you want store data in file="))
print("Apolo Hospital 615")
sequence=1
while(1):
	welcome=input("Do you want to exit Yes or No=")
	if welcome=="Yes":
		sequence
		Name=input("Enter your name=")
		Age=int(input("Enter your Age="))
		Gender=input("Enter your gender=")
		lst.append(sequence)
		
		lst.append(Name)
		lst.append(Age)
		lst.append(Gender)
		print("Data Successfullly entered\n")
		sequence=sequence+1
	elif welcome=="no":
		print("As you wish")
		break
	else:
		print("Please! Enter right option")
stringlst=str(lst)
file=open("Patient.txt",'a')
data=file.write(stringlst)
data=file.write("\n")
# print(os.getcwd())





