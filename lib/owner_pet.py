# lib/owner_pet.py

class Pet:
    PET_TYPES = ["dog", "cat", "rodent", "bird", "reptile", "exotic"]
    all = []

    def __init__(self, name, pet_type, owner=None):
        if pet_type not in Pet.PET_TYPES:
            raise Exception(f"Invalid pet_type: {pet_type}")
        self.name = name
        self.pet_type = pet_type
        self.owner = None  # Will be set when added to owner
        Pet.all.append(self)
        if owner is not None:
            owner.add_pet(self)


class Owner:
    def __init__(self, name):
        self.name = name
        self._pets = []

    def pets(self):
        """Return all pets owned by this Owner"""
        return self._pets

    def add_pet(self, pet):
        """Add a Pet to this Owner, validating type"""
        if not isinstance(pet, Pet):
            raise Exception("pet must be an instance of Pet")
        self._pets.append(pet)
        pet.owner = self

    def get_sorted_pets(self):
        """Return a list of this Owner's pets sorted alphabetically by name"""
        return sorted(self._pets, key=lambda pet: pet.name)
