#Define a class ‘Planet’ having data members: revolution_around_self,
#revolution_around_sun and total satellites. Define appropriate methods to
#initialize and display the values of these data members. Input values for two
#objects and determine which planet is nearer to the sun.
class Planet:
	def __init__(self):
		self.rotation_around_self=int(input("Enter total rotation days::"))
		self.revolution_around_sun=int(input("Enter total rotation days::"))
		self.total_satellites=int(input("Enter total satellites::"))
	def display(self):
		print(f"Roration around self::{self.rotation_around_self}")
		print(f"Revolution_around_sun::{self.revolution_around_sun}")
		print(f"total satellites::{self.total_satellites}")
if __name__=="__main__":
	print("Info about Mercury::")
	Mercury=Planet()
	print("Info about Venus::")
	Venus=Planet()
	print("Info about Mercury::")
	Mercury.display()
	print("Info about Venus::")
	Venus.display()
	
	if Mercury.revolution_around_sun<Venus.revolution_around_sun:
		print("Mercury planet is nearer to the sun")
	else:
		print("Venus planet is nearer to the sun")

	
	
	