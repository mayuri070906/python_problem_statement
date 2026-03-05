#Overload the method ‘findVolume()’ to find volume of cube, cone, cylinder 
#and sphere. Initialize the objects using constructors. Make the use of this().
class Shapes:
	def __init__(self):
		self.s=int(input("Enter side value:"))
		self.radius=int(input("Enter radius value:"))
		self.height=int(input("Enter height value:"))
	def findVolume(self,shape):
		if shape=="cube":
			volume=self.s**3
			print(f"volume of cube:{volume}")
		elif shape=="cone":
			volume=(1/3)*3.14*(self.radius**2)*self.height
			print(f"volume of cone:{volume}")
		elif shape=="cylinder":
			volume=3.14*(self.radius**2)*self.height
			print(f"volume of cylinder:{volume}")
		elif shape=="sphere":
			volume=(4/3)*3.14*(self.radius**3)
			print(f"volume of sphere:{volume}")
if __name__=="__main__":
	s=Shapes()
	s.findVolume("cube")
	s.findVolume("cone")
	s.findVolume("cylinder")
	s.findVolume("sphere")
		

		