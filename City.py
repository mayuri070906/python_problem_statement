class City:
	def __init__(self):
		self.city_name=input("Enter name of city::")
		self.population=float(input("Enter population of the city::"))
		self.administration=input("Enter administration of that city::")
	def display(self):
		print(f"Name of the city::{self.city_name}")
		print(f"Total population of the city::{self.population}")
		print(f"Administration of the city::{self.administration}")
	def averagePopulation(c1,c2,c3):
		average=(c1.population+c2.population+c3.population)//3
		print(f"Average population of all three city::{average}")
if __name__=="__main__":
	c1=City()
	c2=City()
	c3=City()
	print("Information city 1::")
	c1.display()
	print("Information city 2::")
	c2.display()
	print("Information city 3::")
	c3.display()
	City.averagePopulation(c1,c2,c3)
	
		
	