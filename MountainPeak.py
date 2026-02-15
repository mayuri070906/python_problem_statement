class MountainPeak:
	def __init__(self):
		self.name=input("Enter name of the mountain::")
		self.country=input("Enter name of the country::")
		self.height=float(input("Enter mountain heigth in meters::"))
	def display(self):
		print(f"Name::{self.name}")
		print(f"Country::{self.country}")
		print(f"Height in meter::{self.height}")
if __name__=="__main__":
	print("Enter details of first mountain peak:")
	m1=MountainPeak()
	print("Enter details of second mountain peak:")
	m2=MountainPeak()
	print("\nPeak with larger height is:")
	if m1.height>m2.height:
		m1.display()
	elif m1.height<m2.height:
		m2.display()
	else:
		print("Both peaks have equal height.")
		

	