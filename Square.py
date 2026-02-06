class Square:
	def __init__(self):
		self.n=int(input("Enter number::"))
		self.list1=[]
	
	def square(self):
		for i in range(1,self.n+1):
			s=i**2
			self.list1.append(s)
		print(self.list1)
if __name__=="__main__":
	obj=Square()
	obj.square()

			
