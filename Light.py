class Light:
	def __init__(self):
		self.speed_in_water=float(input("Enter speed in water:"))
		self.speed_in_air=float(input("Enter speed in air:"))
		self.speed_in_vaccum=float(input("Enter speed in vaccum:"))
	def display(self):
		print(f"Light speed in water::{self.speed_in_water}")
		print(f"Light speed in air::{self.speed_in_air}")
		print(f"Light speed in vaccum::{self.speed_in_vaccum}")
if __name__=="__main__":
	laserBim=Light()
	laserBim.display()
	if laserBim.speed_in_air==laserBim.speed_in_vaccum:
		print("Laser Bim has Same Travelling speed in Air and Vaccum")
	else:
		print("Laser Bim has not Same Travelling speed in Air and Vaccum")
	