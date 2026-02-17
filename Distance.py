#Declare a class ‘Distance’ having data members dist1, dist2 and dist3.
#Initialize two data members using constructors and store their addition using
#method and display the addition.
class Distance:
	def __init__(self,dist1,dist2):
		self.dist1=dist1
		self.dist2=dist2
		self.dist3=0
	def add_distance(self):
		self.dist3=self.dist1+self.dist2
	def display(self):
		print(f"distance 1:{self.dist1}")
		print(f"distance 2:{self.dist2}")
		print(f"addition of distance:{self.dist3}")
if __name__=="__main__":
	d=Distance(10,30)
	d.add_distance()
	d.display()