class Dog:

	"""A simple dog class"""

	def __init__(self, name):
		self._name = name

	def __str__(self):
		return "Dog"

	def speak(self):
		return "Woof!"

class Cat:

	"""A simple dog class"""

	def __init__(self, name):
		self._name = name

	def __str__(self):
		return "Cat"

	def speak(self):
		return "Meow!"

class DogFactory:
	"""Concrete Factory"""

	def get_pet(self):
		"""Returns a Dog Object"""
		return Dog("Murdock")

	def get_food(self):
		"""Returns a Dog Food Object"""
		return "Dog Food!"

class PetStore:
	def __init__(self, pet_factory=None):
		""" pet_factory is our Abstract factory"""
		self._pet_factory = pet_factory

	def show_pet(self):
		""" Utility method to display the details of the objects returned """

		pet = self._pet_factory.get_pet()
		pet_food = self._pet_factory.get_food()

		print("Our pet is '{}'!".format(pet))
		print("Our pet says hello by '{}'".format(pet.speak()))
		print("Its food is '{}'!".format(pet_food))

#Create a Concrete Factory
factory = DogFactory()

#Create a pet store using our Abstract Factory
shop = PetStore(pet_factory=factory)

#Invoke the utility method to show the details of our pet
shop.show_pet()