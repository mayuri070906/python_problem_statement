class SumOfDigit:
	def __init__(self):
		self.n=input("Enter a number::")
		self.sum=0
		self.length=len(self.n)
	def sumOfDigit(self):
		for i in range(self.length):
			self.sum=self.sum+int(self.n[i])
		print(f"Sum of each digit:{self.sum}")
if __name__=="__main__":
	obj=SumOfDigit()
	obj.sumOfDigit()

