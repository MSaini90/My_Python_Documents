class Employee:
		NoOfLives=5
		pass

Mohit=Employee()
Rohan=Employee()

Mohit.salary=45000
Mohit.role="Techmakny"
Mohit.name="Mohit"

Rohan.salary=4500
Rohan.role="Techno"
Rohan.name="Rohan"

print(Employee.NoOfLives)
print(Mohit.__dict__)
Employee.NoOfLives = 64 #----->@@@@@ class variable only can change by the class not instance variable
# Mohit.NoOfLives=76  #------>Note that instance variable cann't change class variable  
Mohit.NoOfLives=97
print(Mohit.__dict__)
print(Employee.__dict__)