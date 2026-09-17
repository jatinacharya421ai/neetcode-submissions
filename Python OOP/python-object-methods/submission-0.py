class Pet:
    def __init__(self, name: str):
        self.name = name
        self.hunger = 5
    
    def feed(self):
        self.hunger -= 1
        print(f"{self.name} has been fed.")
        print(f"{self.name}'s hunger level: {self.hunger}")

# Create a pet
my_pet = Pet("Fluffy")

# Feed the pet three times
my_pet.feed()
my_pet.feed()
my_pet.feed()
