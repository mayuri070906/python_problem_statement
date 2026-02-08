class WicketKeeper:
	def __init__(self):
		self.player_name=input("Enter name of the player::")
		self.country_name=input("Enter name of the country::")
		self.total_catches=int(input("Enter total catches::"))
		self.total_stumpings=int(input("Enter total_stumpings::"))
	def display(self):
		print(f"Name of the player::{self.player_name}")
		print(f"Country name::{self.country_name}")
		print(f"Total catches::{self.total_catches}")
		print(f"Total stumpings::{self.total_stumpings}")
	def catches_per_stumping(self):
		if self.total_stumpings==0:
			return 0
		return self.total_catches//self.total_stumpings
		
if __name__=="__main__":
	wk1=WicketKeeper()
	wk2=WicketKeeper()
	print("Information about WicketKeeper 1::")
	wk1.display()
	print("Information about WicketKeeper 2::")
	wk2.display()
	r1=wk1.catches_per_stumping()
	r2=wk2.catches_per_stumping()
	if r1>r2:
		print(f"WicketKeeper 1 has taken maximum catches per stumping is:{r1}")
	elif r1<r2:
		print(f"WicketKeeper 2 has taken maximum catches per stumping is:{r2}")
	else:
		print("WicketKeeper 1 & WicketKeeper 2 has taken equal catches per stumping")

