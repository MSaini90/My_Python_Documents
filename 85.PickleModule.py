import pickle

#Pickling a python object
# cars = ["Maruti Suzuki" , "BMW" , "Audi"]
# fileobj = open("Mycar.txt" , "wb")
# pickle.dump(cars , fileobj)
# fileobj.close()

file = "Mycar.txt"
fileobj = open(file , 'rb')
mycar = pickle.load(fileobj)
print(mycar)
print(type(mycar))