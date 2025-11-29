#unit test the functionalities of the digital pet

import unittest
from digital_pet import DigitalPet

#test the pets standardised vitals when the gaem starts
class TestDigitalPet(unittest.TestCase):
    def test_initial_vitals(self):
        pet = DigitalPet("MyPet")
        self.assertEqual(pet.name, "MyPet")
        self.assertEqual(pet.happiness, 5)
        self.assertEqual(pet.hunger, 5)
        self.assertEqual(pet.energy, 5)
        self.assertEqual(pet.age, 0)
        self.assertFalse(pet.sleeping)

