"""
class Animal:  
    def speak(self):  
        print("Animal Speaking")  
class Dog(Animal):  
    def bark(self):  
        print("dog barking")  
				  
class DogChild(Dog):  
    def eat(self):  
        print("Eating bread...")  
d = DogChild()  
d.bark()  
d.speak()  
d.eat()  
"""


class Dad:
    basketball =6

class Son(Dad):
    dance =1
    # basketball = 9
    def isdance(self):
        return f"Yes I dance {self.dance} no of times"

class Grandson(Son):
    dance =6
    guitar = 1

    def isdance(self):
        return f"Jackson yeah!" \
            f"Yes I dance very awesomely {self.dance} no of times"

darry = Dad()
larry = Son()
harry = Grandson()

print(harry.isdance())
print(harry.basketball)

# electronic device
# pocket gadget
# phone



