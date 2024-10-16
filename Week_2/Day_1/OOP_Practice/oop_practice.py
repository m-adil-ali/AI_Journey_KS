class Animal:
    def __init__(self):
        self.name = "Unknown"
        self.age = 0
        
    def breed(self,breed):
        self.breed = breed
        
    def type(self,type):
        self.type = type
    
    #def setter(self,)
    
    def getter(self):
        print(f"Name: {self.name}, Age: {self.age}, Breed: {self.breed}, Type: {self.type}")
    
janwar = Animal()

janwar.name = "khiii"
janwar.age = 3
janwar.breed('russian')
janwar.type('dangerous')

janwar.getter()


# coin2 = coin.Coin()
# coin2.get()