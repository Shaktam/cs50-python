x=int(input("What's x? "))
y= int(input("what's y? "))
z=x+y
print(z)

x1=float(input("What's x? "))
y1= float(input("what's y? "))
z1=x1+y1
print(z1)

#round(number[,ndigit])
#[] is always optional it is to specify a digit if we don't want to specify a digit we can only specify a number

z1=round(x1+y1)
print(f"{z1:,}")

z2=round(x1+y1,2)
print(z2)
z3=x1/y1
#.2f is a place holder for floating number, %d for int, %s for string and %o for octal 
print(f"{z:d}")
print(f"{z2:.2f}")

def main():
    x=int(input("what's x?"))
    print("x squared is", square(x))
def square(n):
    return n*n
main()    