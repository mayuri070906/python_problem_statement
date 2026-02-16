class Air1:
	def __init__(self,per_of_oxygen=0,per_of_nitrogen=0,humidity=0):
		self.per_of_oxygen=per_of_oxygen
		self.per_of_nitrogen=per_of_nitrogen
		self.humidity=humidity
	def display(self):
		print(f"per_of_oxygen::{self.per_of_oxygen}")
		print(f"per_of_nitrogen::{self.per_of_nitrogen}")
		print(f"humidity::{self.humidity}")
if __name__=="__main__":
	o1=int(input("Enter per_of_oxygen::"))
	n1=int(input("Enter per_of_nitrogen::"))
	h1=int(input("Enter humidity::"))
	air1=Air1(o1,n1,h1)

	o2=int(input("Enter per_of_oxygen::"))
	n2=int(input("Enter per_of_nitrogen::"))
	h2=int(input("Enter humidity::"))
	air2=Air1(o2,n2,h2)

	print("information 1::")
	air1.display()

	print("information 2::")
	air2.display()

	if air1.humidity>air2.humidity:
		print("Air 1 has higher humidity.")
	elif air1.humidity<air2.humidity:
		print("Air 2 has higher humidity.")
	else:
		print("Air 1 and Air 2 have equal humidity")


	

	
	



