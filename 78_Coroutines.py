def searcher():
	import time
	# Some 4 seconds time consuming task
	book = "This is a book on Mohit Saini and it is related to coding "
	time.sleep(4)

	while True:
		text = (yield)
		if text in book:
			print("Your text is there in the book")
		else:
			print("Text is not in this book")

search = searcher()
print("Search started")
next(search)
print("Next method run")
search.send("Mohit")
input("press any key")
search.send("Hrk")
input("press any key")
search.send("Saini")
input("press any key")
search.send("Hello")
input("press any key")
search.send("thanks")
search.close()
search.send("MFFK")



