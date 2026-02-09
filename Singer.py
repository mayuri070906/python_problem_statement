class Singer:
	def __init__(self):
		self.singer_name=input("Enter name of the singer::")
		self.sang_songs=int(input("Enter total sang songs::"))
		self.total_awards=int(input("Enter total awards::"))
	def display(self):
		print(f"Name of the singer::{self.singer_name}")
		print(f"Total sang songs::{self.sang_songs}")
		print(f"Total awards::{self.total_awards}")
	def calculateAward(self):
		if self.total_awards==0:
			return 0
		return self.sang_songs//self.total_awards
if __name__=="__main__":
	s1=Singer()
	s2=Singer()
	print("Information about singer 1::")
	s1.display()
	print("Information about singer 2::")
	s2.display()
	a1=s1.calculateAward()
	a2=s2.calculateAward()
	if a1>a2:
		print("singer 1 has taken maximum awards per song")
	elif a1<a2:
		print("singer 1 has taken maximum awards per song")
	else:
		print("singer 1 and singer 2 has equal awards per song")


	
