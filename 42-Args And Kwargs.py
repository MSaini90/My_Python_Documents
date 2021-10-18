def func(normal,*args,**kwargsbala):
	print(normal)
	for item in args:
		print(item, end = " ")
	
	print("\nThese are some gandu matherchod except harry bro")
	for key,values in kwargsbala.items():
		print(f"{key} is {values}")


nameList=["Mohit Saini","Ronaldo","Ratan Tata","Ali gilani","Pappu Congress wale"]
 
normal = "I am normal"

kw = {"Rohan":"Monitor", "Harry":"Fitness Instructor",
      "The Programmer": "Coordinator", "Shivam":"Cook"}
func(normal,*nameList,**kw)          


