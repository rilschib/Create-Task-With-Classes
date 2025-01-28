import random
import time
class Lotto:
    def __init__(prizemoney, winnumber):
        winnumber = random.randrange(1, 25, 1)
        prizemoney = float(random.randrange(1000, 100000, 500))