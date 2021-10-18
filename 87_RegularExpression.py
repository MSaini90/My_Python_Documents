import re 

mystr = ''''Mohit is locaiaiaited in Rigai, Latvia and is part of the Commercial Printing Industry.
				has 1 total employees across  of its locations and generates  sales (USD).
				D&B Hoovers provides sales leads and 545-4444 sales intelligence data on over 120 million
				 companies like
				Brazzers around the world, including contacts, financials, and competitor information. 
				To witness the full depth and breadth for our data and for industry leading sales
				 intelligence
				tools, take D&B Hoovers for a test drive. Try D&B Hoovers free. 34555-02222'''   

# Findall , search , split , finditer , sub

"""
All Meta character

[] = A set of characters
\  = Signals a special sequence (can also be used to escape special characters)  
.  = Any character (Except newline character)
^  = starts with 
$  = End with 
*  = Zero or more occurrences
+  = One or more occurrences
{} = Exactly the specified number of occurrences
|  = Either or 
() = Capture the group  

"""


# Meta-Characters
# patt = re.compile(r"Brazzers")    #print(r"\n")
# patt = re.compile(r".")
# patt = re.compile(r".total")
# patt = re.compile(r'^Mohit')
# patt = re.compile(r'free$') #nahi chala
# patt = re.compile(r"ai*")
# patt = re.compile(r"a*i*")   # ZERO YA KITNE BHI i ho
# patt = re.compile(r"ai+") 
# patt = re.compile(r"ai{1}") 
# patt = re.compile(r"(ai){2}") #match 2 ai and make group  
# patt = re.compile(r"sa{1}|and")

# matches = patt.finditer(mystr)
# for match in matches:
# 	print(match)



#Special Characters 
"""
\A Returns a match if the specified characters are
 at the beginning of the string

\b Returns a match where the specified characters are 
at the beginning (or at the end) of a word 

\B Returns a match where the specified characters are 
present , but NOT at the beginning (or at the end) of 
a word 

\d Returns a match where the string contains digits (numbers from 0-9)

\D Returns a match where the string does not contains digits 

\s Returns a match where the string contains a whitwe space characters

\S Returns a match where the string does not contains a whitwe space characters 

\W Returns a match where the string Does not contains any word characters

\w Returns a match where the string contains any word characters
(Characters from a to z, digits form 0-9, and the underscore_ character)

\Z Returns a match if the specified characters are at end of the string
"""

# Special Sequences
# patt = re.compile(r"\AMohit")
# patt = re.compile(r" for\b ")
# patt = re.compile(r" free\b ")
# patt = re.compile(r"Brazzers")
patt = re.compile(r'\d{5}-\d{5}')

matches = patt.finditer(mystr)
for match in matches:
	print(match)
	# print(mystr[281:289])