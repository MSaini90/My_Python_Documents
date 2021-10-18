import time
i=1
initial=time.time()
while(i<=24):
	print(i,end=" ")
	time.sleep(1)
	i+=1
print("\nWhile loop's executiontime is",time.time()-initial)
for i in range(1,24+1):
	print(i,end=" ")
print("\nfor loop's executiontime is",time.time()-initial)

localtime=time.asctime(time.localtime(time.time()))
print(localtime)
