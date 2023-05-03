"""
Arithmetic Operator
+, _, *, /, %

data types
int
float
str
bool
list
used def function and return statement
"""
x= int(input("What is x? "))

if x%2==0:
    print("x is even")
else:
    print("x is odd")    

# we don't have any built-in instead we can create our own function
def main():
    x= int(input("What is x? "))
    if is_even(x):
        print("x is even")
    else:
        print("x is odd") 
def is_even(n):
    if n%2==0:
        return True
    else:
        return False
main()             
# or
def main():
    x= int(input("What is x? "))
    if is_even(x):
        print("x is even")
    else:
        print("x is odd") 
def is_even(n):
    return True if n%2==0 else False
main()        