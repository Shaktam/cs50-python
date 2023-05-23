"""Vanity Plates
CS50 license plate

In Massachusetts, home to Harvard University, it’s possible to request a vanity license plate for your car, with your choice of letters and numbers instead of random ones. Among the requirements, though, are:

“All vanity plates must start with at least two letters.”
“… vanity plates may contain a maximum of 6 characters (letters or numbers) and a minimum of 2 characters.”
“Numbers cannot be used in the middle of a plate; they must come at the end. For example, AAA222 would be an acceptable … vanity plate; AAA22A would not be acceptable. The first number used cannot be a ‘0’.”
“No periods, spaces, or punctuation marks are allowed.”
In plates.py, implement a program that prompts the user for a vanity plate and then output Valid if meets all of the requirements or Invalid if it does not. Assume that any letters in the user’s input will be uppercase. Structure your program per the below, wherein is_valid returns True if s meets all requirements and False if it does not. Assume that s will be a str. You’re welcome to implement additional functions for is_valid to call (e.g., one function per requirement).

def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    ...


main()
Hints
Recall that a str comes with quite a few methods, per docs.python.org/3/library/stdtypes.html#string-methods.
Much like a list, a str is a “sequence” (of characters), which means it can be “sliced” into shorter strings with syntax like s[i:j]. For instance, if s is "CS50", then s[0:2] would be "CS"."""
def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(plate):
    sp_ch=['.',' ','!','?',':',',']
    if not (2<=len(plate)<=6) :
        return False
    elif not plate[:2].isalpha():
        return False
    elif plate in sp_ch:
        return False
    else:
        plate.upper()
    number=False
    for char in plate:
        if char.isdigit():
            if char=='0' and not number:
                return False
            number=True
        elif char.isalpha():
            if number:
                return False
        else:
            return False
    return True

main()