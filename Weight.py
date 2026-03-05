#Overload the method ‘findWeight()’ in your class to convert the weight given 
#in ounces, pounds and tons to kilograms. Use constructor to input values.
class Weight:
	def __init__(self):
		self.ounces=int(input("Enter weight in ounces:"))
		self.pounds=int(input("Enter weight in pounds :"))
		self.tons=int(input("Enter weight in tons:"))
	def findWeight(self,unit):#method overloadding in python is not possible....If you write multiple methods with the same #name, Python keeps only the last one and overrides the previous ones.
		if unit=="ounces":
			kg=self.ounces*0.02835
			print(kg)
		elif unit=="pounds":
			kg=self.pounds*0.4536
			print(kg)
		else:
			kg=self.tons*907.2
			print(kg)
if __name__=="__main__":
	obj=Weight()
	print("Ounces to kg:")
	obj.findWeight("ounces")
	print("pounds to kg:")
	obj.findWeight("pounds")
	print("tons to kg:")
	obj.findWeight("tons")



