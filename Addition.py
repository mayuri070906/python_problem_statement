class Addition:
	def __init__(self):
		self.n=int(input("Enter your choice number::"))
		self.sum=0
	
	def addition(self):
		for i in range(1,self.n+1):
			self.sum=self.sum+(1/i)
		print(self.sum)
if __name__=="__main__":
	obj=Addition()
	obj.addition()
	

		