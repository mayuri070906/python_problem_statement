class Product:
	def __init__(self,product_id="",product_name="",price=0):
		self.product_id=product_id
		self.product_name=product_name
		self.price=price
	def display(self):
		print(f"Product ID:{self.product_id}")
		print(f"Product Name:{self.product_name}")
		print(f"Price::{self.price}")
	def Total_price(self,other):
		total=self.price+other.price
		print(f"Total price::{total}")
if __name__=="__main__":
	p_id1=input("Enter product id::")
	p_name1=input("Enter product name::")
	pri1=int(input("Enter price::"))
	p1=Product(p_id1,p_name1,pri1)

	p_id2=input("Enter product id::")
	p_name2=input("Enter product name::")
	pri2=int(input("Enter price::"))
	p2=Product(p_id2,p_name2,pri2)

	p1.display()
	p2.display()

	p1.total_price(p2)	

	