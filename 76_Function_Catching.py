# import time

# def SomeWork(n):
# 	time.sleep(n)
# 	return nj


# if __name__ == '__main__':
# 	print("Now running some work")
# 	SomeWork(3)
# 	print("Done calling again....")
# 	SomeWork(3)
# 	print("Called Again")






import time
from functools import lru_cache

@lru_cache(maxsize=32)
def Some_work(n):
	#Some task taking n seconds
	time.sleep(n)
	return n


if __name__ == '__main__':
	print("Now running some function")
	Some_work(3)
	print("h")
	Some_work(1)
	print("h77")
	Some_work(4)
	print("h666")
	Some_work(5)
	print("Done ... Calling again")
	Some_work(3)
	print("HA ha aha")                
	# Some_work(6)
	# print("ok")
	# Some_work(9)
	# print("Done ... Calling again")
	input("Enter any word 'Or' character")
	Some_work(3)
	print("Called again")
	# Some_work(10)
