class Language:
	def __init__(self):
		self.state=input("Enter state::")
		self.population=int(input("Enter population::"))
	def display(self):
		print(f"Name of the state::{self.state}")
		print(f"Population::{self.population}")
if __name__=="__main__":
	L1=Language()
	L2=Language()
	print("Information about state 1::")
	L1.display()
	print("Information about state 2::")
	L2.display()
	if L1.population>L2.population:
		print(f"Language spoken in {L1.state} is more widely spoken")
	elif L1.population<L2.population:
		print(f"Language spoken in {L2.state} is more widely spoken")
	else:
		print("Both language are equally spoken")