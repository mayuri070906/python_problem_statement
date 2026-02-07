class Month:
	def __init__(self):
		self.month_name=input("Enter name of the month::")
		self.total_days=int(input("Enter total days of month::"))
		self.total_hoildays=int(input("Enter total hoildays of month::"))
	def countWorkingDay(self):
		self.total_working_days=self.total_days-self.total_hoildays
		return self.total_working_days
	def display(self):
		print(f"Name of the name::{self.month_name}")
		print(f"Total days of the month::{self.total_days}")
		print(f"Total hoildays of the month::{self.total_hoildays}")
if __name__=="__main__":
	m1=Month()
	m2=Month()
	m1.countWorkingDay()
	m2.countWorkingDay()
	print("Information about month 1::")
	m1.display()
	print("Information about month 2::")
	m2.display()
	if m1.total_working_days>m2.total_working_days:
		print("month 1 having maximum working days")
	elif m1.total_working_days<m2.total_working_days:
		print("month 2 having maximum working days")
	else:
		print("Both month having same working days")


		