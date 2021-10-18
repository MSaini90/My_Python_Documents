# lst=[ ["Mohit",3],["Rohit",43],["Rajkishor",45],["Roshan",45] ]
# Dict1=dict(lst)
# # print(Dict1)
# for item,lollypop in Dict1.items():
	# print(item,"lolly is =",lollypop)

lst=[float,int,45,3,45,2,3,4,566,55,]
for item in lst:
	if str(item).isnumeric() and item>6:
		print(item)