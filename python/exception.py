#synatax Error- It is something which can be easily solved
#ValueError- shows it's not right datatype- value of variable is typed incorrect
#Name error-  

x=int(input("What is x?"))
print(f"x is {x}")

if x:
    x=int(input("What is x?"))
    print(f"x is {x}")
else:
    print("x is not an interger")     
#or
try:
    x=int(input("What is x?"))
    print(f"x is {x}")
except ValueError:
    print("x is not an interger")  


try:
    x=int(input("What is x?")) 
except ValueError:
    print("x is not an interger")  
else:
    print(f"x is {x}")
#or
while True:
    try:
        x=int(input("What is x?")) 
    except ValueError:
        print("x is not an interger")  
    else:
        break
print(f"x is {x}")    

#or 

while True:
    try:
        x=int(input("What is x?")) 
        break
    except ValueError:
        print("x is not an interger")  
                
print(f"x is {x}")    

while True:
    try:
        x=int(input("What is x?")) 
        break
    except ValueError:
        print("x is not an interger")  
    else:
        break            
print(f"x is {x}")    

def main():
    x=get_int()
    print(f"x is {x}")  

def get_int():
    while True:
        try:
            x=int(input("What is x?")) 
        except ValueError:
            print("x is not an interger")  
        else:
            break 
    return x               

main()



def main():
    x=get_int()
    print(f"x is {x}")  

def get_int():
    while True:
        try:
            x=int(input("What is x?"))  
        except ValueError:
            print("x is not an interger")  
        else:
            return x  
                  
main()
        
def main():
    x=get_int()
    print(f"x is {x}")  

def get_int():
    while True:
        try:
            x= int(input("What is x?"))  
            return x
        except ValueError:
            print("x is not an interger")  
                  
main()   


def main():
    x=get_int()
    print(f"x is {x}")  

def get_int():
    while True:
        try:
            return int(input("What is x?"))  
        except ValueError:
            print("x is not an interger")  
                  
main()    


def main():
    x=get_int()
    print(f"x is {x}")  

def get_int():
    while True:
        try:
            return int(input("What is x?"))  
        except ValueError:
            pass
main()    


def main():
    x=get_int("What is x?")
    print(f"x is {x}")  

def get_int(prompt):
    while True:
        try:
            return int(input(prompt))  
        except ValueError:
            pass
main()    