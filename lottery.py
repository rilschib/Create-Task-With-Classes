import random
import time
from player_class import *
from randomber import *
print("What name should we put this under?")
name = input()
wallet = float(random.randrange(100, 10000, 1))
while wallet > 9:
    print(name, " has $",wallet," in their wallet. don't ask how we know this.")
    print("winning prize is $", randomber.prizemoney, ", pick a number between 1 and 25, and if your number matches the random number, you win the prize money.")
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