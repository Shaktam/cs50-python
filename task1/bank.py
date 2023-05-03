greet=input("Greeting: ").lower().strip()
if greet.startswith("hello"):
    print("$0")
elif greet.startswith("h", 0):
    print("$20")
else:
    print("$100")
