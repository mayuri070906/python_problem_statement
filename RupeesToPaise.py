class RupeesToPaise:
	def __init__(self):
		self.price=float(input("enter prize of the item in rupees::"))

	def rupeesToPaise(self):
		paice=int(self.price*100)
		print(f"The price in paice::{paice}")

if __name__=="__main__":
	obj=RupeesToPaise()
	obj.rupeesToPaise()
	

		
		
