class Monitor:
	def __init__(self):
		self.company_name=input("Enter company name:")
		self.type=input("Enter type of monitor:")
		self.width=int(input("Enter width of monitor:"))
		self.height=int(input("Enter height of monitor:"))
		self.screen_size=int(input("Enter size of screen in inch::"))
		self.resolution=0.0
	def calculateResolution(self):
		self.resolution=(((self.width)**2+(self.height)**2)**0.5)//self.screen_size
		return self.resolution
	def display(self):
		print(f"company name:{self.company_name}")
		print(f"Type of monitor:{self.type}")
		print(f"total resolution:{self.resolution:.2f} PPI")
if __name__=="__main__":
	m1=Monitor()
	m2=Monitor()
	m1.calculateResolution()
	m2.calculateResolution()
	print("Information about monitor 1::")
	m1.display()
	print("Information about monitor 2::")
	m2.display()
	
	if m1.resolution>m2.resolution:
		print(f"maximum resolution is monitor 1")
	elif m1.resolution<m2.resolution:
		print(f"maximum resolution is monitor 2")
	else:
		print("Both resolution is same resolution")



	
	
		