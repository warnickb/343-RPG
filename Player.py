
import random
from Weapon import Weapon

class Player:
     def __init__(self):
          self.HP = random.randint(125, 150)
          self.attackValue= random.randint(10, 20)
          