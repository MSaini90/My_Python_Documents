import random
lst=["snake","water","gun"]

i=1
_computer_point=0
_human_point=0
print("                     ##@@@@@@&&& Snake Water Gun Game  @@@&&&&&@@@@@               \n")
try:
	times=int(input("How many times you want a play Game="))
except Exception as e:
	print("You cann't Enter any other value Except numeric",e)

print("                     @@@@@@@@@@@@@ WELCOME @@@@@@@@@@                  \n ")
while(i<=times):
	ychoice=input("Enter any one option * snake * , * water * , and * gun * for game=")
	choice=random.choice(lst)
	if ychoice==choice:
		print("Both choices tie\n")

	elif ychoice=="snake" and  choice=="gun" :
		_computer_point=	_computer_point+1
		print("Computer Won")
		print(f"computer Guess {choice} and Your Guess {ychoice} \n")

	elif ychoice=="snake" and choice=="water":
		_human_point=_human_point+1
		print("You won")
		print(f"Your Guess {ychoice} and Computer guess {choice} \n" )

	elif ychoice=="gun" and choice=="snake":
		_human_point=_human_point+1
		print("You won")
		print(f"Your Guess {ychoice} and Computer guess {choice} \n")
	
	elif ychoice=="gun" and choice=="water":
		_computer_point=_computer_point+1
		print("Computer won") 
		print(f"Computer guess {choice} and Your Guess {ychoice} \n")
		
	elif ychoice=="water" and choice=="snake":
		_computer_point=_computer_point+1
		print("Computer won") 
		print(f"Computer guess {choice} and Your Guess {ychoice} \n")

	
	elif ychoice=="water" and choice=="gun":
		_human_point=_human_point+1
		print("You won") 
		print(f"Your Guess {ychoice} and Computer guess {choice} \n")
	else:
		print("Sorry! you entered wrong choice")
	i+=1
print("&&&&&&###@@@@@ GAME END @@@@##@@@@@@&&***\n")
if _human_point>_computer_point:
	print("You Won the Game")
elif _human_point==_computer_point:
	print("Game tie")
else:
	print("Computer won the game")
		


