class RupeesToDollers:
	def __init__(self):
		self.R=int(input("Enter rupees::"))
		self.E=83.0

	def rupeesToDollers(self):
		D=self.R//self.E
		print(f"Rupees in dollar::{D}")

if __name__=="__main__":
	obj=RupeesToDollers()
	obj.rupeesToDollers()

