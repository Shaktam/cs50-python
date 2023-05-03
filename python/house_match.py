# match is used for the same variable with different values and _ used as catch all 
name = input("What is your name? ")

if name== "Tanny":
    print("Gryffindor")
elif name== "Harry":
    print("Gryffindor")    
elif name== "Ron":
    print("Gryffindor")
elif name== "Hermeion":
    print("Gryffindor") 
elif name== "Draco":
    print("Slytherin")
else:
    print("Who?")  

#or
if name== "Tanny" or name== "Harry" or  name== "Ron" or name== "Hermeion":
    print("Gryffindor")
elif name== "Draco":
    print("Slytherin")
else:
    print("Who?")   

 

match name:
    case "Tanny":
        print("Gryffindor")
    case "Harry":
        print("Gryffindor")
    case "Ron":
        print("Gryffindor")
    case "Hermeion":
        print("Gryffindor")            
    case "Draco":
        print("Slytherin")
    case _:
        print("Who? ")

#or

match name:                
    case "Hermeion" | "Tanny" | "Ron" | "Harry":
        print("Gryffindor")            
    case "Draco":
        print("Slytherin")
    case _:
        print("Who? ")