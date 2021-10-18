"""
Python JSON:->  JSON stands for JavaScript Object Notation, which is a widely used data 
format for data interchange on the web. JSON is the ideal format for organizing data 
between a client and a server. Its syntax is similar to the JavaScript programming language.
The main objective of JSON is to transmit the data between the client and the web server.
It is easy to learn and the most effective way to interchange the data. It can be used with 
various programming languages such as Python, Perl, Java, etc.

JSON mainly supports 6 types of data type In JavaScript:

1-String
2-Number
3-Boolean
4-Null
5-Object
6-Array



Working with Python JSON:-> Python provides a module called json. Python supports 
standard library marshal and pickle module, and JSON API behaves similarly as these
 library. Python natively supports JSON features.

The encoding of JSON data is called Serialization. Serialization is a technique where 
data transforms in the series of bytes and transmitted across the network.

The deserialization is the reverse process of decoding the data that is converted
into the JSON format.
This module includes many built-in functions.

Let's have a look at these functions:
import json  
print(dir(json))  
"""

"""
Serializing JSON:-> Serialization is the technique to convert the Python objects to JSON
. Sometimes, computer need to process lots of information so it is good to store that 
information into the file. We can store JSON data into file using JSON function. The 
json module provides the dump() and dumps() method that are used to transform Python object.


Python objects are converted into the following JSON objects. The list is given below:

Sr.	   Python Objects	  JSON

1.        	Dict	     Object
2.	    list, tuple	   Array
3.         	Str	       String
4.	    int, float      Number
5.       	 True         true
6.	      False	        false
7.	      None	         null

"""
                     #@@@@@@@@ Harry @@@@@@@@@@

#@@@@@@@&&&&&&&&&&&&&&&&&&&&&&&&&&&&&##  Deserializing of python data to JSON  &&&&&$$$##@@@@

import json
# data = '{"Name":"Mohit","Age":"29"}'
# parsed = json.loads(data)
# # print(type(parsed))
# print(parsed["Name"])


#@@@@@@@&&&&&&&&&&&&&&&&&&&&&&&&&&&&&##  Serializing of python data to JSON  &&&&&$$$##@@@@

# data2 = {
#     "channel_name":"ms-techno",
# 		"cars":["Audi","BMW","Lamborgini"],
# 		"BAg":('bidi_No_578'),
# 		"isbad" :False
#     }

# print(type(data2))
# print(data2)
# jscomp = json.dumps(data2)
# print(jscomp)
# print(type(jscomp))



# @@@@@@@@@@@@  NEXT   @@@@@@@@@@@@@@######

#@@@@@@@&&&&&&&&&&&&&&&&&&&&&&&&&&&&&##  Serializing of python data to JSON  &&&&&$$$##@@@@

# #@@@@@@@@@@ Using dump function @@@@@&&&&& 

# Python provides a dump() function to transmit(encode) data in JSON format. It accepts
# two positional arguments, first is the data object to be serialized and second is 
# file-like object to which the bytes needs to be written.

# student = {
#                "Name":"Mohit Saini",
# 							 "Age":"23",
# 							 "Class":"BCA",
# 							 "Subjects":['Computer Networking','Python','Graph theory', 'php']
#           }

# with open ("data.json","w") as write_file:
# 	json = json.dump(student,write_file)


#@@@@@@@@@@ Using dumps function @@@@@&&&&& 

# The dumps() function is used to store serialized data in the Python file. 
# It accepts only one argument that is Python data for serialization. 
# The file-like argument is not used because we aren't not writing data to disk. 
# Let's consider the following example:

# student = {
# 							  "Name" : "Mohit Saini",
# 							  "Class" : "BCA",
# 							  "Age" : 50
#            } 

# b = json.dumps(student)
# print(b)



# JSON supports primitive data types, such as strings 
# and numbers, as well as nested list, tuples and objects.

# #Python  list conversion to JSON  Array   
# print(json.dumps(['Welcome', "to", "javaTpoint"]))  
  
# #Python  tuple conversion to JSON Array   
# print(json.dumps(("Welcome", "to", "javaTpoint")))  
  
# # Python string conversion to JSON String   
# print(json.dumps("Hello"))  
  
# # Python int conversion to JSON Number   
# print(json.dumps(1234))  
  
# # Python float conversion to JSON Number   
# print(json.dumps(23.572))  
  
# # Boolean conversion to their respective values   
# print(json.dumps(True))  
# print(json.dumps(False))  
  
# # None value to null   
# print(json.dumps(None))   



#@@@@@@@&&&&&&&&&&&&&&&&&&&&&&&&&&&&&##  Deserializing of python data to JSON  &&&&&$$$##@@@@

# Deserialization is the process to decode the JSON data into the Python objects. The json module
#  provides two methods load() and loads(), which are used to convert JSON data in actual Python 
#  object form.

# SR.	   JSON	    Python
# 1.   	Object	   dict
# 2.	  Array    	 list
# 3.	  String	   str
# 4.	number(int)  int
# 5.	  true	     True
# 6.	 false      False
# 7.	null	      None



 
#@@@@@@@@@@ Using load() function######@@@@@@

# The load() function is used to deserialize the JSON data to Python object from the file. 


# student = {
# 						"Name" : "Mohit",
# 						"Age" : 46,
# 						"Class" : "BCA"
# 					}
# with open ("data1.json","w") as write_file:
# 	json.dump(student,write_file)

# with open ("data1.json","r") as read_file:
# 	b = json.load(read_file)
# print(b)


#@@@@@@@@@@ Using loads() function######@@@@@@

# The json module also provides loads() function, which is used to convert JSON data to Python object.
# It is quite similar to the load() function. Consider the following example:

a = ["Mathew" , "Peter" , (10,46,57,38), {"Country" : "INDIA"}]

#Python into json 
b = json.dumps(a)
print(b)
#JSON into pyton object
c = json.loads(b)
print(c)

# a = (10,20,30,40,50,60,70)  
# # print(type(a))  
# b = json.dumps(a)
# print(type(b))  
# # print(type(json.loads(b)))  


#Sometimes we need to analyze and debug a large amount of JSON data. It can be done
# by passing additional arguments indent and sort_keys in json.dumps() and json.dump() methods. 

# import json  
  
# person = '{"Name": "Andrew","City":"English", "Number":90014, "Age": 23,"Subject": ["Data Structure","Computer Graphics", "Discrete mathematics"]}'  
  
# per_dict = json.loads(person)  
  
# print(json.dumps(per_dict, indent = 5, sort_keys= True))  
