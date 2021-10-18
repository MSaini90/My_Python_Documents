"""
The object st called the second 
constructor whereas both have the same configuration. 
The first method is not accessible by the st object. 
Internally, the object of the class will always call
the last constructor if the class has multiple constructors.

Note: The constructor overloading is not allowed in Python.

"""

"""
class Student:  
    def __init__(self):  
        print("The First Constructor")  
    def __init__(self):  
        print("The second constructor")  
st = Student()  Output will be=The second constructor
"""

"""
Need for multiple constructors Multiple constructors are required when 
one has to perform different actions on the instantiation of a class. 
This is useful when the class has to perform different actions on different parameters. 
The class constructors can be made to exhibit polymorphism in three ways which are listed 
below.

1-Overloading constructors based on arguments.
2-Calling methods from __init__.
2-Using @classmethod decorator.
"""



"""
1=>Overloading constructors based on arguments:

The constructor overloading is done by checking conditions for the arguments 
passed and performing required actions. For example, consider passing an argument to the 
class sample, 

If the parameter is an int, the square of the number should be the answer.
If the parameter is a String, the answer should be “Hello!!”+string.
If the parameter is of length greater than 1, the sum of arguments should be
 stored as the answer.
 """

"""

class sample: 

    def __init__(self, *args): 
        # if args are more than 1 
        # sum of args 
        if len(args) > 1: 
            self.ans = 0
            for i in args: 
                self.ans += i 
  
        # if arg is an integer 
        # square the arg 
        elif isinstance(args[0], int): 
            self.ans = args[0]*args[0] 
  
        # if arg is string 
        # Print with hello 
        elif isinstance(args[0], str): 
            self.ans = "Hello! "+args[0]+"."
  
  
s1 = sample(1, 2, 3, 4, 5) 
print("Sum of list :", s1.ans) 
  
s2 = sample(5) 
print("Square of int :", s2.ans) 
  
s3 = sample("GeeksforGeeks") 
print("String :", s3.ans)

"""

"""
Output
Sum of list : 15
Square of int : 25
String : Hello! GeeksforGeeks.

In the code above, the instance variable was ans, but its values differ based on the
arguments. Since a variable number of arguments for the class, *args is used which is a 
tuple that contains the arguments passed and can be accessed using an index. In the case
of int and string, only one argument is passed and thus accessed as 
args[0] (the only element in the tuple).
"""


"""
2-Calling methods from __init__

A class can have one constructor __init__ which can perform any action when 
the instance of the class is created. This constructor can be made to different 
functions that carry out different actions based on the arguments passed. 
Now consider an example : 

If the number of arguments passed is 2, then evaluate the expression x = a2-b2
If the number of arguments passed is 3, then evaluate the expression y = a2+b2-c.
If more than 3 arguments have been passed, then sum up the squares, divide it by
 the highest value in the arguments passed.
"""


class eval_equations: 
  
  # single constructor to call other methods 
    def __init__(self, *inp): 
  
        # when 2 arguments are passed 
        if len(inp) == 2: 
            self.ans = self.eq2(inp) 
  
        # when 3 arguments are passed 
        elif len(inp) == 3: 
            self.ans = self.eq1(inp) 
  
        # when more than 3 arguments are passed 
        else: 
            self.ans = self.eq3(inp) 
  
    def eq1(self, args): 
        x = (args[0]*args[0])+(args[1]*args[1])-args[2] 
        return x 
  
    def eq2(self, args): 
        y = (args[0]*args[0])-(args[1]*args[1]) 
        return y 
  
    def eq3(self, args): 
        temp = 0
        for i in range(0, len(args)): 
            temp += args[i]*args[i] 
          
        temp = temp/max(args) 
        z = temp 
        return z 
  
  
inp1 = eval_equations(1, 2) 
inp2 = eval_equations(1, 2, 3) 
inp3 = eval_equations(1, 2, 3, 4, 5) 
  
print("equation 2 :", inp1.ans) 
print("equation 1 :", inp2.ans) 
print("equation 3 :", inp3.ans) 







"""
3-Using @classmethod decorator

This decorator allows a function to be accessible without instantiating the class. 
The functions can be accessed both by the instance of the class and the class itself.
The first parameter of the method that is declared as classmethod is cls, which is
like the self of the instance methods. Here cls refer to the class itself. 
This proves to be very helpful to use multiple constructors in Python and is
a more Pythonic approach considered to the above ones. Consider the same example 
used above. Evaluate different expressions based on the number of inputs.

"""


"""
class eval_equations: 
  
    # basic constructor 
    def __init__(self, a): 
        self.ans = a 
  
    # expression 1 
    @classmethod
    def eq1(cls, args): 
        
      # create an object for the class to return 
        x = cls((args[0]*args[0])+(args[1]*args[1])-args[2]) 
        return x 
  
    # expression 2 
    @classmethod
    def eq2(cls, args): 
        y = cls((args[0]*args[0])-(args[1]*args[1])) 
        return y 
  
    # expression 3 
    @classmethod
    def eq3(cls, args): 
        temp = 0
  
        # square of each element 
        for i in range(0, len(args)): 
            temp += args[i]*args[i] 
  
        temp = temp/max(args) 
        z = cls(temp) 
        return z 
  
  
li= [1, 2, 3]
# i = 0
  
# loop to get input three times 
# while i < 3: 
  
# inp = li[i] 

# no.of.arguments = 2 
if len(li) == 2: 
    q = eval_equations.eq2(li) 
    print("equation 2 :", q.ans) 

# no.of.arguments = 3 
elif len(li) == 3: 
    p = eval_equations.eq1(li) 
    print("equation 1 :", p.ans) 

# More than three arguments 
else: 
    p = eval_equations.eq3(li) 
    print("equation 3 :", p.ans) 
  
    #increment loop         
    # i += 1
"""





