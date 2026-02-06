class ReverseOrder:
	def __init__(self):
		self.n=int(input("enter a number::"))
		self.num=str(self.n)
	def ReverseOrder(self):
		self.reverse=str(self.num[::-1])
		print(self.reverse)
if __name__=="__main__":
	obj=ReverseOrder()
	obj.ReverseOrder()


		
		
