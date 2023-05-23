"""Suppose that a machine sells bottles of Coca-Cola (Coke) for 50 cents and only accepts coins in these denominations: 25 cents, 10 cents, and 5 cents.

In a file called coke.py, implement a program that prompts the user to insert a coin, one at a time, each time informing the user of the amount due. Once the user has inputted at least 50 cents, output how many cents in change the user is owed. Assume that the user will only input integers, and ignore any integer that isn’t an accepted denomination."""
def main():
    print("1 coco cola bottle costs 50 cent.")
    print("If you want Coco-cola, Machine will accept only 25 cents, 10 cents, and 5 cents coin: ")
    total_cost= 50
    coins=[25,10,5]
    while total_cost >0:
        print(f"Amount Due: {total_cost}")
        inserted_coin=int(input("Inserted Coin: "))
        if inserted_coin in coins:
            total_cost=total_cost-inserted_coin
    print(f"Change Owed: {abs(total_cost)}")
main()
 