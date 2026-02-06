class BankAccount:
	def __init__(self):
		self.acc_no=int(input("Enter account number::"))
		self.acc_username=input("Enter username::")
		self.acc_balance=float(input("Enter opening balance::"))
	
	def display(self):
		print(f"Account username::{self.acc_username}")
		print(f"Account number::{self.acc_no}")
		print(f"Account balance::{self.acc_balance}")
	def get_balance(self):
		return self.acc_balance
if __name__=="__main__":
	print("Bank detail acc_username 1::")
	b1=BankAccount()
	print("Bank detail acc_username 2::")
	b2=BankAccount()
	b1.display()
	b2.display()
	if b1.get_balance()>b2.get_balance():
		print("Account balance of user 1 is greater than user 2")
	elif b2.get_balance()>b1.get_balance():
		print("Account balance of user 2 is greater than user 1")
	else:
		print("Account balance is both user is equal")
	

	