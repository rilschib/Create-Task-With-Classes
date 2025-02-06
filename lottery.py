import random
import time
import re
class Player:
    def __init__(wallet, name):
        self.balance = balance
        self.name = name
fee = 10
win = 15
bigwin = 100
grandprize = 777
icons = "A" "1" "!"
x = "1" or "!"
y = "11" or "!!"
z = "1111" or "!!!!"
a = "!!!!!!" or "111111"
J = "AAAAAA"
j = "AAAA"
b = "11"
c = "!!"
d = "AA"
e = "1"
f = "!"
g = "A"
r = "["
l = "]"
n = "[\n]"
etc = "A", "1", "!"
lsgrand = (r,a,l,n,r,a,l,n,r,a,l)
lsgrandls2 = ((lsgrand))

lsbig1 = (r,a,l,n,r,a,l,n,r,a,l,n)
lsbig2 = (r,e,d,e,l,n,r,e,d,e,n,r,e,d,e,l)
lsbig3 =  (r,d,f,d,l,n,r,d,f,d,l,n,r,d,f,d,l)
lsbig = (lsbig1 or lsbig2 or lsbig3)
lsbigls2 = ((lsbig1),(lsbig2),(lsbig3))

lswin1 = (r,b,x,b,l,n,r,b,x,b,l,n,r,b,x,b,l)
lswin2 = (r,c,x,c,l,n,r,c,x,c,l,n,r,c,x,c,l)
lswin3 = (r,e,f,x,f,e,l,n,r,e,f,x,e,l,n,r,e,f,x,e,l)
lsreg = (lswin1 or lswin2 or lswin3)
lsregls2 = ((lswin1),(lswin2),(lswin3))

winning = (lsreg or lsbig or lsgrand)

winning2 = ((lsbigls2),(lsregls2),(lsgrandls2))

rand1 = (random.sample(icons, 3))
rand2 = (random.sample(icons, 3))
rand3 = (random.sample(icons, 3))
rand4 = (random.sample(icons, 3))
rand5 = (random.sample(icons, 3))
rand6 = (random.sample(icons, 3))

Randall_The_Gambling_Mechanism = "[",(str(rand1,rand2,rand3)),"]","\n","["
print = (re.sub("[() ,[]]", "",Randall_The_Gambling_Mechanism))
print("What name should we put this under?")
name = input()
balance = float(random.randrange(1000, 10000, 10))
while True:
    print(name, " your balance is $",balance,"and the grand prize is", grandprize, ". to roll, type roll.")
    userin = input().strip().lower()
    if userin == "roll":
        balance -= float(fee)
        print("roll the slots!")
        print(Randall_The_Gambling_Mechanism)
        if Randall_The_Gambling_Mechanism == lsgrand:
            print(f"Grand prize of $",grandprize," was won!")
            balance ,= float(grandprize)
        if Randall_The_Gambling_Mechanism == lsbig:
            print(f"big sized win of $",bigwin," was won!")
            balance ,= float(bigwin)
        if Randall_The_Gambling_Mechanism == lsreg :
            print(f"win get! won $", win, "!")
        if Randall_The_Gambling_Mechanism not in winning2:
            print("loser.")
if not userin("roll"):
    print("dumbo")