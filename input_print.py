user_name = input("\nHey, What is your nmae: ")
print(f"Welcome, {user_name}! We're glad to have you here!")

class Pet:
    def __init__(self,name,tricks,food):
        self.name = name
        self.tricks = tricks
        self.food = food
        self.health = 0 
        self.energy = 0
    
    def walk(self):
        self.energy += 5
        self.health += 5

    def eat(self):
        self.health += 10
        self.energy += 10
    
    def sleep(self):
        self.health += 15
        self.energy += 15

    def play(self):
        self.energy -= 10
        self.health += 10

class Person:
    def __init__(self,f_name,l_name,pet,pet_tricks,pet_food):
        self.f_name = f_name
        self.l_name = l_name
        self.pet = Pet(pet,pet_tricks,pet_food)
    
    def go_walk(self):
        print(f"{self.f_name} walks with their pet {self.pet}")
        return self

