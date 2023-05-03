#Function- Function an action or verb (eg, print)
#argument- input to a function
#variable- acts as a container and carries the value
# Psuedocode- todolist
name= input("What's your name? ")
#sep Parameter only separtes the given argument but end parameter can help you to write the output in single line 
print("Hello,", sep=" ",end=" ")
print(name)
"""
#remove white space from string
name =name.strip()
#capitalize username
name=name.capitalize()
#captitalzing the title like capitalize every first letter of word
name = name.title()
"""

#or we can write in single line
name =name.strip().title()
#split user name into first name and last name
first,last = name.split(" ")
print(f"Hello, {first}", sep=" ")
#ways to write hello world
print("Hello,", name)
print("Hello,",name, sep=" ")
print("hello,", end=" ")
print(name)
print(f"hello, {name}")
print("Hello, \"Shakti\"")

#def is a function help us to create our own function
