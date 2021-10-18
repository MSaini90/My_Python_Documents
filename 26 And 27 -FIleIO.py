"""
"r"-open file for read=default mode
"w"- open a file for writing
"x"-Creates file if not exits
"a"-Add more content to a file
"t"-text mode=default mode
"b"-binary mode
"+"-read and write mode
"""

# f=open("MohitRead.txt")
# print(f.readlines())
# print(f.readline())
# print(f.readline())
# print(f.readline())



"""
f=open("MohitRead.txt")
content=f.read()
for line in content:
	print(line,end="")
	"""
# print(content)

"""
f=open("MohitRead.txt")
content=f.read(37777)
print("1",content)
content=f.read(3)
print("2",content)
f.close() """

# *********---#File Writing in python ************=====---
# f=open("MohitWrite.txt","a")
# a=f.write("Mohit is a Unique person\n") #a--for reading character
# print(a)
# f.close()

#Handle read and write both
# f=open("MohitWrite.txt","r+")
# print(f.read())
# f.write

f=open("MohitRead.txt")
print("initially File pointer exist",f.tell())
content=f.read()
print(content)
print("After reading the file the file pointer exist",f.tell())
f.seek(10)
print("After reading the file the file pointer eist",f.tell())