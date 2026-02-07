class Tennis:
	def __init__(self):
		self.player_name=input("Enter a player name::")
		self.country_name=input("Enter a country name::")
		self.total_championships=int(input("Enter total championships::"))
	def display(self):
		print(f"Name of the player::{self.player_name}")
		print(f"Name of the country::{self.country_name}")
		print(f"Total championships::{self.total_championships}")
if __name__=="__main__":
	t1=Tennis()
	t2=Tennis()
	t3=Tennis()
	print("Information about player 1::")
	t1.display()
	print("Information about player 2::")
	t2.display()
	print("Information about player 3::")
	t3.display()
	if t1.total_championships>t2.total_championships and t1.total_championships>t3.total_championships:
		print("player 1 is real champion")
	elif t2.total_championships>t1.total_championships and t2.total_championships>t3.total_championships:
		print("player 2 is real champion")
	else:
		print("player 3 is real champion")


	



