"""Suppose that a machine sells bottles of Coca-Cola (Coke) for 50 cents and only accepts coins in these denominations:
 25 cents, 10 cents, and 5 cents.

In a file called coke.py, implement a program that prompts the user to insert a coin, one at a time, each time informing 
the user of the amount due. Once the user has inputted at least 50 cents, output how many cents in change the user is 
owed. Assume that the user will only input integers, and ignore any integer that isn’t an accepted denomination."""

def main():
    
    InsertCoin()

def InsertCoin():
    Tmoney=50
    while Tmoney > 0 :

        print(f"amount Due: ${Tmoney}")
        coin = int(input(" Please insert coin: "))
        if coin == 25 or coin == 10 or coin == 5:
            Tmoney = Tmoney - coin
            if Tmoney == 0:
                owned = 0
                print(f"Change Owed: {owned}")
                break
            elif Tmoney < 0:
                owned = Tmoney*-1
                print(f"Change Owed: {owned}")
                break
            elif Tmoney > 0:
                continue
        else:
            print("Don't allow coin, please insert coins of 25, 10 or 5 cents")

if __name__==("__main__"):
    main()