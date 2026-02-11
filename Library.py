class Library:
	def __init__(self):
		self.total_books=int(input("Enter total books::"))
		self.total_mazagines=int(input("Enter total mazagines::"))
		self.total_periodicals=int(input("Enter total periodicals::"))
		self.Total_all_books=0
	def allBooks(self):
		self.Total_all_books=self.total_books+self.total_mazagines+self.total_periodicals
		return self.Total_all_books
	def display(self):
		print(f"Total Books:{self.total_books}")
		print(f"Total mazagines:{self.total_mazagines}")
		print(f"Total periodicals:{self.total_periodicals}")
if __name__=="__main__":
	success=Library()
	yash=Library()
	print("info success_library:")
	success.display()
	print("info yash_library:")
	yash.display()
	success_total=success.allBooks()
	yash_total=yash.allBooks()
	if success_total > yash_total :
		print("success library is having largest collection of all books")
	elif success_total < yash_total :
		print("yash library is having largest collection of all books")
	else:
		print("success and yash library are having same collection of all books")



	
		