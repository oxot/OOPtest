class Drink():
	__price = 100

	def __init__(self, volume):
		self.volume = volume

	def getprice(self):
		return self.volume*self.__price		


class Coffee(Drink):
	__price = 60

	def __init__(self, volume, strength, milk):
		super().__init__(volume)
		self.strength = strength
		self.milk = milk
		if milk:
			self.name = "Cappuccino"
		else:
			self.name = "Espresso"

	def getprice(self):
		return (self.strength+self.milk)*self.__price*self.volume

	def receit(self, table):
		print(self.name, round(0.1*self.volume, 1), "table", table, " Price:", self.getprice())


class Tea(Drink):
	def __init__(self, volume, type):
		super().__init__(volume)
		self.type = type
		self.name = "tea"

	def receit(self, table):
		print(self.type, self.name, round(0.1*self.volume, 1), "table", table
			           ," Price:", self.getprice())


coffee = Coffee(2, 1, 1)
coffee.receit(12)
tea = Tea(3, "Green")
tea.receit(9)