answer= input("What is answer to the Great Question of Life, the Universe and Everything? ").lower().strip()
# if answer == "42" or answer =="Fourty Two" or answer == "forty-two":
#     print("Yes")
# else:
#     print("No")
match answer:
    case "42" | "Forty Two" | "forty two" | "forty-two" :

        print("Yes")
    case _:
        print("No")