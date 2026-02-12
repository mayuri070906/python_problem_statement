#Define a class ‘Forest’ having data members: area_in_sq_cm,
#count_of_animals. Define appropriate methods to initialize and display the
#values of these data members. Input values for two objects and determine
#which forest is having more space per animal.
class Forest:
	def __init__(self):
		self.area_in_sq_cm=int(input("Enter Area in sq cm::"))
		self.count_of_animals=int(input("Enter total animals in forest::"))
	def space_per_animals(self):
		if self.count_of_animals==0:
			return 0
		return self.area_in_sq_cm/self.count_of_animals
	def display(self):
		print(f"Area of the forest::{self.area_in_sq_cm}")
		print(f"Total animals in forest::{self.count_of_animals}")
if __name__=="__main__":
	amazon=Forest()
	tadu=Forest()
	print("Amazon forest information::")
	amazon.display()
	print("tadu forest information::")
	tadu.display()
	f1=amazon.space_per_animals()
	f2=tadu.space_per_animals()
	if f1>f2:
		print("amazon forest is having more space per animal.")
	elif f1<f2:
		print("tadu forest is having more space per animal.")
	else:
		print("amazon and  tadu forest is having equal space per animal.")



	