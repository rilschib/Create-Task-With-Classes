import random
import time
class player:
    def __init__(wallet, name):
        self.wallet = wallet
        self.name = name
lotteryman = '( ͡° ͜ʖ ͡°)'
wallet = float(random.randrange(100, 10000, 1))
winnumber = random.randrange(1, 26, 1)
prizemoney = float(random.randrange(1000, 100000, 500))
while wallet > 9:
    print(lotteryman)
    print(name, " has $",wallet," in your wallet. don't ask how we know this.")
    print("winning prize is $",prizemoney, ", pick a number between 1 and 26, and if your number matches the random number, you win the prize money.")
    time.sleep(2)
    input("pick your number: ")
    if input == winnumber:
        print(f"you won! your prize is $",prizemoney)
        if input == winnumber:
             wallet += prizemoney
    elif input is not winnumber:
        print("you lost. you are out by $10")
        wallet -= 10
        time.sleep(2)