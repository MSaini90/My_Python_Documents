
print("Welcome To Google")
print("*----***----**")
while(1):
		
	Dic={}
	Name=input("Enter Employee's Name=")
	Age=int(input("Enter Employee's Age="))
	Salary=int(input("Enter Employee's salary="))
	Address=input("Enter Employee's Address=")
	Dic.update({"Name":Name,"Age":Age,"Salary":Salary,"Address":Address})
	print(Dic)
	print("Will you want to perform these step Enter '1 for Keys' or '2 for delete',0 for nothing")
	yes=int(input())

	if yes==1:
		print(Dic.keys())
	elif(yes==2):
		data=input("Enter your delete Data=")
		del Dic["data"]
		print(dic)
	else:
		print("As your wish")
		
