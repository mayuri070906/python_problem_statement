class Reverse:
	def __init__(self):
		self.n=int(input("Enter your number:"))
		self.rev=0
	def reverse(self):
		while self.n>0:
			self.digit=self.n%10
			self.rev=self.rev*10+self.digit
			self.n//=10
		print(f"Reverse Number:{self.rev}")
if __name__=="__main__":
	obj=Reverse()
	obj.reverse()