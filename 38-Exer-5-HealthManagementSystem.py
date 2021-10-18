import datetime
def gettime():
    return datetime.datetime.now()
def log_file(lgfile):
	name=input("\nEnter name whose file you want to log ms-for Mohit,r-for ronaldo,m-for messi-->")
  	#**********ACTIVITY of MOHIT******########
	if name=="ms":
		activity=input("What you want to enter diet or exercise-->")

		if activity=="diet":
			lst=[]
			type=int(input("\nWhat kind of food did Mohit eat today="))
			sequence=1
			print("Enter food's name")
			for type in range(1,type+1):
				print(sequence,end="=")
				foodfile=input()                 
				lst.append(foodfile)
				sequence=sequence+1
			f=open("MohitFood.txt","a")
			food1=str(lst)
			f.write(str([str(gettime())])+":"+food1+"\n")
			print("Successfullly Entered")

		elif activity=="exercise":
			lst=[]
			type=int(input("What kind of exercise did Mohit do today="))
			sequence=1
			print("\nEnter Daily's exercise")
			for item in range(1,type+1):
				print(sequence,end="=")
				Exercise=input()
				lst.append(Exercise)
				sequence=sequence+1
			f=open("MohitExcercise.txt","a")
			exer1=str(lst)
			f.write(str([str(gettime())])+":"+exer1+"\n")
			print("Successfullly Entered")
		else:
			print("Please1 Enter valid activity")

  #************ACTIVITY FOR RONALDO**********#######
	elif name=="r": 
		activity=input("What you want to write diet or exercise-->")

		if activity=="diet":
			lst=[]
			type=int(input("What kind of food did Ronaldo eat today="))
			sequence=1
			print("\nEnter daily's food names")
			for item in range(1,type+1):
				print(sequence,end="=")
				foodfile=input()
				lst.append(foodfile)
				sequence=sequence+1
			f=open("RonaldoFood.txt","a")
			food2=str(lst)
			f.write(str([str(gettime())])+":"+food2+"\n")
			print("Successfullly Entered")

		elif activity=="exercise":
			lst=[]
			type=int(input("What kind of exercise did Ronaldo do today="))
			sequence=1
			print("\nEnter Daily's Exercise")
			for item in range(1,type+1):
				print(sequence,end="=")
				Exercise=input()
				lst.append(Exercise)
				sequence=sequence+1
			f=open("RonaldoExcercise.txt","a")
			exer2=str(lst)
			f.write(str([str(gettime())])+":"+exer2+"\n")
			print("Successfullly Entered")
		else:
			print("Please! Enter valid activity")

#**********ACTIVITY FOR MESSI***********########
	elif name=="m":
		activity=input("What you want to write diet or exercise-->")
		
		if activity=="diet":
			lst=[]
			type=int(input("\nWhat kind of food did Messi eat today="))
			sequence=1
			print("Enter food's names")
			for type in range(1,type+1):
				print(sequence,end="=")
				food=input()
				lst.append(food)
				sequence=sequence+1
			f=open("MessiFood.txt","a")
			food3=str(lst)
			f.write(str([str(gettime())])+":"+food3+"\n")
			print("Successfullly Entered")

		elif activity=="exercise":
			lst=[]
			type=int(input("\nWhat kind of exercise did Messi do today="))
			sequence=1
			print("Enter Daily's Exercise")
			for item in range(1,type+1):
				print(sequence,end="=")
				Exercise=input()
				lst.append(Exercise)
				sequence=sequence+1
			f=open("MessiExcercise.txt","a")
			exer3=str(lst)
			f.write(str([str(gettime())])+":"+exer3+"\n")
			print("Successfullly Entered")
		else:
			print("Please! Enter valid activity")
	else:
		print("Please! Enter valid name")	

#*******************Retrieve Operation start Now********$$$&&&&&&&&&&		

def _retrieve(rtfile):
  name=input("Enter name whose file you want to retrieve ms-for Mohit,r-for ronaldo,m-for messi-->")

#**********______FILE RETRIEVE OF RONALDO
  if name=="r":
			activity=input("What you want to retrieve diet or exercise=")
			if activity=="diet":
				try:	
					with open("RonaldoFood.txt","rt") as f:
						read=f.read()
						print(read)
				except IOError:
				  print("Sorry! there are no present data in this perticular file")
			elif activity=="exercise":
				try:
					with open("RonaldoExcercise.txt","rt") as f:
						read=f.read()
						print(read)
				except IOError:
					print("Sorry! there are no present data in this perticular file")
			else:
					print("Please1 Enter valid activity")
			
			

#@@@@@@@@@@@@@@@@@@@FILE RETRIEVE FOR MESSI********000000000
  elif name=="m":
			
			activity=input("What you want to retrieve diet or exercise=")
			if activity=="diet":
				try:
					with open("MessiFood.txt","rt") as f:
						read=f.read()
						print(read)
				except IOError:
					print("Sorry! there are no data present in this perticular file")
			elif activity=="exercise":
				try:
					with open("MessiExcercise.txt","rt") as f:
						read=f.read()
						print(read)
				except IOError:
					print("Sorry! there are no data present in this perticular file")
			else:
				print("Please1 Enter valid activity")
#@@@@@@@@@@@@@@@@@@@FILE RETRIEVE FOR Mohit********000000000 
  elif name=="ms":
			activity=input("What you want to retrieve diet or exercise=")
			if activity=="diet":
				try:
					with open("MohitFood.txt","rt") as f:
						read=f.read()
						print(read)
				except IOError:
					print("Sorry! there are no data present in this perticular file")
			elif activity=="exercise":
				try:
					with open("MohitExcercise.txt","rt") as f:
						read=f.read()
						print(read)
				except IOError:
					print("Sorry! there are no data present in this perticular file")
			else:
				print("Please1 Enter valid activity")

	
  else:
		  print("Please! Enter valid name")
while True:
	take=input("\n\n                What do you want @@@-- *logfile* or *retrieve* --@@@\n                 ")
	if take=="logfile":
		log_file(take)
	elif take=="retrieve":
		_retrieve(take)
	else:
		print("Please Enter valid operation")