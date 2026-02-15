
class Forests1:
	def __init__(self,area_in_sq_cm=0,count_of_animals=0):
		self.area_in_sq_cm=area_in_sq_cm
		self.count_of_animals=count_of_animals
	def space_per_animals(self):
		if self.count_of_animals==0:
			return 0
		return self.area_in_sq_cm/self.count_of_animals
	def display(self):
		print(f"Area of the forest::{self.area_in_sq_cm}")
		print(f"Total animals in forest::{self.count_of_animals}")
if __name__=="__main__":
	print("Enter details of First forest:")
	a1=int(input("Enter area in square cm:"))
	c1=int(input("Enter count of animals:"))
	f1=Forests1(a1,c1)
	print("Enter details of second forest:")
	a2=int(input("Enter area in square cm:"))
	c2=int(input("Enter count of animals:"))
	f2=Forests1(a2,c2)
	s1 = f1.space_per_animals()
	s2 = f2.space_per_animals()
	print("Determine which forest is having less space per animal")
	if s1<s2:
		print("forest 1 is having less space per animal.")
		f1.display()
	elif s1>s2:
		print("forest 2 is having less space per animal.")
		f2.display()
	else:
		print("forest 1 and forest 2 is having equal space per animal.")

