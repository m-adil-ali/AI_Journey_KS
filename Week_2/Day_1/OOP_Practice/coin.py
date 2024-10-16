import random
import oop_practice
class Coin:
    def __init__(self):
        self.__side = 'Tails'
        
    def flip(self):
        if random.randint(0,1) == 0:
            self.__side = 'Heads'
        else:
            self.__side = 'Tails'
    
    def get(self):
        return self.__side

coin1 = Coin()
coin1.__side = 'ulta'
coin1.flip()
coin1.flip()
t = coin1.get()
print(t)
#print(coin1.get())

janwar1 = oop_practice.Animal()

janwar1.name = 'shankar'
janwar1.age = 1
janwar1.breed('asian')
janwar1.type('jangali')
janwar1.getter()