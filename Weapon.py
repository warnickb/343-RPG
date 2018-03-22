#Weapon class that the player will use. I changed the weapon power
#values to do a bit more damage.
#Used https://docs.python.org/3/library/random.html for randint help
#test

import random

class Weapon:
    def __init__( self , other = True ):
        if( other == True ):
            
            r = random.randint(1 , 3)
            
            if r == 1:
                self.name = "Sour Straw"
                self.amount = 10
                self.power = 2
                
            elif r == 2:
                self.name = "Chocolate Bar"
                self.amount = 5
                self.power = 5
                
            elif r == 3:
                self.name = "Nerd Bomb"
                self.amount = 1
                self.power = 15
		
        else :
            self.name = "Hershey Kisses"
            self.amount = 1000
            self.power = 1