"""i=0
while(True):
	if i+1<5:	
	 i=i+1
	continue
	print(i+1,end=" ")
	if(i==44):
		break
	i=i+1"""
print("Enter number")
i=0
while(True):
	n=int(input())
	i=i+1
	if n>=100:
	  print("OUT OF RANGE\n")
	  break
	else:
		print("Try Again")
		continue
print(f"You played {i} times")
  

