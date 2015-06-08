class Animal:
	def __init__(self, name, age, weight):
		self.name = name
		self.age = age
		self.weight = weight

	def eat(self):
		self.weight += 1



class Panda(Animal):

	def __init_(self, name, age, weight, skill):
		super().__init__(name, age, weight)
		self.skill = skill

	def _sleep(self):
		self.__weight += 10

	def eat(self):
		print("NOM NOM NOM NOM")
		self.weight += 10
	
	def __hash__(self):
		return hash(self.name + str(self.weight))

dimcho = Panda("Dimcho", 10, 1500)
