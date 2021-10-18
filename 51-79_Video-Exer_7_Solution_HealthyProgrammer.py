from pygame import mixer
from datetime import datetime
from time import time
def musicloop(file,stopper):
	mixer.init()
	mixer.music.load(file)
	mixer.music.play()
	while True:
		_user_input=input()
		if _user_input==stopper:
			mixer.music.stop()
			break

def lognow(msg):
	with open("mylogs.txt","a") as f:
		f.write(f"{msg} {datetime.now()}\n")
init_water=time()
init_eyes=time()
init_exercise=time()
watersecs=5
eyesecs=20
exsecs=10



while True:
	if time()-init_water>watersecs:
		print("\n\n\n\n\n\n\n\n                                  @@@----Have a nice day---@@\n                             ")
		print('Water drinknig time Enter "drank" for stop the alarm')
		musicloop('Kudi.mp3','drank')
		init_water=time()
		lognow('Drank Water At')

	
	if time()-init_eyes>eyesecs:	
		print('Eyes exercise time Enter "eyedone" for stop the alarm')
		musicloop('Cola.mp3','eyedone')
		init_eyes=time()
		lognow('Eyedone At')

	if time()-init_exercise>exsecs:	
		print('Now exercise time Enter "exerdone" for stop the alarm ')
		musicloop('Call.mp3','exerdone')
		init_exercise=time()
		lognow('Exercise At')