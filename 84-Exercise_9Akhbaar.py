# def speak (str):
# 	from  import Dispatch

# 	speak = Dispatch("SAPI.SpVoice")

# 	speak.Speak(str)

# if __name__ == '__main__':
# 	speak("You are the best launda in this world")


def speak(str):

	from win32com.client import Dispatch
	speak=Dispatch("SAPI.SpVoice")
	speak.Speak(str)


if __name__ == ' __main__ ':
	speak("You are the best my friend");
     
# print("Our Api KEY=5792c91dffe2443ca645775c3cfeb2e3")