
import random

class NPC:
    def __init__(self):
        pass
    def Power(self):
        pass
    
class Person:
    def __init__(self,Monster):
        self.name = "Person"
        self.HP = 100
    def Power(self):
        return 0
    
class Zombie:
    def __init__(self):
        self.name = "Zombie"
        self.HP = random.randint(50, 100)
    def Power(self):
        power = random.randint(0, 10)
        return power
    
class Vampire:
    def __init__(self):
        self.name = "Vampire"
        self.HP = random.randint(100, 200)
    def Power(self):
        power = random.randint(10,20)
        return power

class Ghoul:
    def __init__(self):
        self.name = "Ghoul"
        self.HP = random.randint(40, 80)
    def Power(self):
        power = random.randint(15, 30)
        return power
        
class Werewolves:
    def __init__(self):
        self.name = "Werewolf"
        self.HP = 200
    def Power(self):
        power = random.randint(0, 40)
        return power
    