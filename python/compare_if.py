"""
Conditional Operator

```
<
>
<=
>=
!=
==
```
```
if
elif
else
or
and
```
"""

x=int(input("what is x? "))
y=int(input("what is y? "))

if x<y:
    print("x is less than y")

if x>y:
    print("x is greater than y")

if x==y:
    print("x is equal to y")

# In this case it checks every condition before giving result,
# Instead of using if for every condition use elif which checks the condition if is true give result and stop, or if it's false it checks next condition   
# additionally, we can use else in case if we checked all the condition we need and we dont need to check any other condition use else to skip using condition

#elif
if x<y:
    print("x is less than y")

elif x>y:
    print("x is greater than y")

elif x==y:
    print("x is equal to y")

# else
if x<y:
    print("x is less than y")

elif x>y:
    print("x is greater than y")

else:
    print("x is equal to y")    

# conditions

if x>y or x<y:
    print("x is not equal to y")

else:
    print("x is equal to y")     

# simplied version either

if x==y:
    print("x is equal to y")

else:
    print("x is not equal to y")     

#or
if x!=y:
    print("x is not equal to y")

else:
    print("x is equal to y")      