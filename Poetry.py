class Poetry:
	def __init__(self):
		self.poem_title=input("Enter name of the poem::")
		self.poet_name=input("Enter name of the port::")
		self.total_verses=int(input("Enter total verses of poem::"))
	def display(self):
		print(f"poem title::{self.poem_title}")
		print(f"poet name::{self.poet_name}")
		print(f"total verses::{self.total_verses}")
if __name__=="__main__":
	poem1=Poetry()
	poem2=Poetry()
	print("Information about poem1::")
	poem1.display()
	print("Information about poem2::")
	poem2.display()
	if poem1.total_verses>poem2.total_verses:
		print(f"{poem1.poem_title} poem is longest")
	elif poem1.total_verses<poem2.total_verses:
		print(f"{poem2.poem_title} poem is longest")
	else:
		print(f"{poem1.poem_title} and {poem1.poem_title} poems are equal lines")