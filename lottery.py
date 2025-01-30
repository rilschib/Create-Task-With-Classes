import random
import time
class Player:
    def __init__(wallet, name):
        self.balance = balance
        self.name = name
win = 10
bigwin = 100
biggerwin = 1000
grandprize = 10000
icons = ["A", "@", "^", "%", "~"]
machine = "_______\n|0 0 0|\n|-=*=-|\n|_____|"
print("What name should we put this under?")
name = input()
balance = float(random.randrange(1000, 10000, 10))
while True:
    print(name, " your balance is $",balance,"and the grand prize is", grandprize, ". to roll, type roll.")
    userin = input().strip().lower()
    if userin == "roll":
        print("roll the slots!")
        print(machine)
        random.choice(icons)
else:
    print("dumbo")
