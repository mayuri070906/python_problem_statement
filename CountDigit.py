class CountDigit:
	def __init__(self):
		self.n=int(input("Enter a number::"))
		self.count=0
	def countDigit(self):
		while self.n>0:
			self.n//=10
			self.count+=1
		print(f"Totol digit::{self.count}")
if __name__=="__main__":
	obj=CountDigit()
	obj.countDigit()

		
