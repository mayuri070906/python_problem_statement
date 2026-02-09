class Passport:
	def __init__(self):
		self.Name=input("Enter name ::")
		self.nationality=input("Enter nationality::")
		self.passport_number=int(input("Enter passport number::"))
	def display(self):
		print(f"Username::{self.Name}")
		print(f"Nationality::{self.nationality}")
		print(f"Passport number::{self.passport_number}")
if __name__=="__main__":
	p1=Passport()
	p2=Passport()
	p3=Passport()
	print("Information about username 1::")
	p1.display()
	print("Information about username 2::")
	p2.display()
	print("Information about username 3::")
	p3.display()

	
