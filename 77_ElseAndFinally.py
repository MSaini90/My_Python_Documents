f1= open ("MS.txt")

try :
	f2=open ("Mohit77.txt")

except Exception as e:
	print(e)

except EOFError as e:
	print("EOFError has occurred",e)    #We can use multiple Except statement in program

except IOError as e:
	print("IOError has occurred",e)	

print("Important Stuff")

# else:
	
# 	print("This will only run only if execpt is not running")


finally:
  print("Run this anyway")
	f1.close()
	f2.close()

