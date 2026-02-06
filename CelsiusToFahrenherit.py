class CelsiusToFahrenherit:
	def __init__(self):
		self.F=int(input("Enter temperature in Fahrenherit::"))

	def celsiusToFahrenherit(self):
		C=int((self.F-32)/1.8)
		print(f"Temperature in celcius::{C} C")

if __name__=="__main__":
	obj=CelsiusToFahrenherit()
	obj.celsiusToFahrenherit()

