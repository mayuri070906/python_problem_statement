class Cone:
	def __init__(self):
		self.radius=int(input("Enter radius of the cone::"))
		self.height=int(input("Enter height of the cone::"))
		self.volume=0.0
	def findVolume(self):
		self.volume=(1/3)*3.14*(self.radius**2)*self.height
		return self.volume

if __name__=="__main__":
	c1=Cone()
	c1.findVolume()
	c2=Cone()
	c2.findVolume()
	if c1.volume>c2.volume:
		print("Radius of cone with greater volume:", c1.radius)
	elif c1.volume<c2.volume:
		print("Radius of cone with greater volume:", c2.radius)
	else:
		print("Both cones have equal volume")
		
	
