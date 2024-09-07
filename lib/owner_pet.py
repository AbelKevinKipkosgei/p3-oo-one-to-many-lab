class Pet:
    PET_TYPES = ["dog", "cat", "rodent", "bird", "reptile", "exotic"]
    all = []


    def __init__(self, name, pet_type, owner=None):
        self.name = name
        self.pet_type = pet_type
        self.owner = owner

        if pet_type not in Pet.PET_TYPES:
            raise TypeError("Pet is not in Pet Types")
        
        Pet.all.append(self)

    def __repr__(self):
        return f"{self.name}, {self.pet_type}, {self.owner}"

class Owner:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f"{self.name}"
    
    def pets(self):
        all_pets = [pet for pet in Pet.all if pet.owner == self]
        print(all_pets)
        return all_pets

    def add_pet(self, pet):
        if not isinstance(pet, Pet):
            raise TypeError("The pet must be an instance of the Pet class.")
        
        pet.owner = self

    def get_sorted_pets(self):
        all_pets = self.pets()
        sorted_pets = sorted(all_pets, key=lambda pet: pet.name)
        print(sorted_pets)
        return sorted_pets

pet1 = Pet("Bartolo", "cat")
pet2 = Pet("Bobby", "dog")

owner = Owner("Joy Ruth")
owner.add_pet(pet1)
owner.add_pet(pet2)

owner.pets()

owner.get_sorted_pets()
