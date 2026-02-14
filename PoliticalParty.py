class PoliticalParty:
	def __init__(self):
		self.name=input("Enter of the party::")
		self.total_MLAs=int(input("Enter Number of MLAs::"))
		self.total_MLCs=int(input("Enter Number of MLCs::"))
		self.total_MPs=int(input("Enter Number of MPs::"))

	def total_leaders(self):
		return self.total_MLAs+self.total_MLCs+self.total_MPs

	def display(self):
		print(f"political party name::{self.name}")
		print(f"Total_MLAs::{self.total_MLAs}")
		print(f"Total_MLAs::{self.total_MLCs}")
		print(f"Total_MLAs::{self.total_MPs}")
		print(f"total_leaders::{self.total_leaders()}")
		
if __name__=="__main__":
	party1=PoliticalParty()
	party2=PoliticalParty()
	print("information political party 1::")
	party1.display()
	print("information political party 2::")
	party2.display()
	total_elected=(party1.total_MLAs+party1.total_MPs)+(party2.total_MLAs+party2.total_MPs)
	print(f"Total leaders elected by citizens from both parties::{total_elected}")
	
	

	

	


