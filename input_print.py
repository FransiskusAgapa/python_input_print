# user_name = input("\nHey, What is your nmae: ")
# print(f"Welcome, {user_name}! We're glad to have you here!")

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
    def __init__(self,f_name,l_name,pet_name,pet_tricks,pet_food):
        self.f_name = f_name
        self.l_name = l_name
        self.pet = Pet(pet_name,pet_tricks,pet_food)
    
    def go_walk(self):
        print(f"{self.f_name} walks with their pet, {self.pet.name}!")
        return self

f_name = input("\nHi, I am bot! What is your first name: ")
l_name = input("What is your last name: ")
pet_name = input("What is your pet name: ") # assuming this person has a pet / with a pet
pet_tricks = input("What is your pet's favorite trick: ")
pet_food = input("What is your favorite food: ")

person_one = Person(f_name,l_name,pet_name,pet_tricks,pet_food)
person_one.go_walk()

update_data = input("\nWould you like to update the data: ").lower()
while(update_data == "y" or len(update_data) > 1):
    if(len(update_data)>1 ):
        print("\n> Invalid Input [ y/Y for Yes | n/N for No ]\n")

    f_name = input("\nHi, I am bot! What is your first name: ")
    l_name = input("What is your last name: ")
    pet_name = input("What is your pet name: ") # assuming this person has a pet / with a pet
    pet_tricks = input("What is your pet's favorite trick: ")
    pet_food = input("What is your favorite food: ")

    person_one = Person(f_name,l_name,pet_name,pet_tricks,pet_food)
    person_one.go_walk()

    update_data = input("would you like to update the data: ").lower()
    
print("\nThank you for your input! :)")
