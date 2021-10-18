import os

# print(dir(os)) #Object Introspection-It tells us what we can do with it

# print(os.name)

# print(os.getcwd())  #Function return current working directory

# os.chdir("C://")    # Function change the current working directory

# print(os.getcwd())  

# f = open("Saini.txt")

lst = os.listdir("D://") #Return the all files and Folder Related to location
# print(lst)
# print(type(lst))
# os.mkdir("This45")   # Function is use for making directory

# os.makedirs("This/That") # Function is use for making directories

# os.rename("Saini.txt" , "MS233.txt")  # Function is use for Rename of the directories
# print("Successfully Renamed")
# print(os.environ.get('Path'))

# print(os.path.join("C:/" , "//MS.txt"))

print(os.path.exists("C://Program Files")) #Function tells the path is exists or not

# print(os.path.isfile("C://Program Files/"))