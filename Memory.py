#Overload the method ‘convertTo()’ with different parameters to convert 
#terabytes, gigabytes and megabytes to equivalent bytes value.
class Memory:
	def __init__(self):
		self.TB=int(input("Enter value in terabytes:"))
		self.GB=int(input("Enter value in gigabytes:"))
		self.MB=int(input("Enter value in megabytes:"))
	def convertTO(self,TB=0,GB=0,MB=0):
		if TB!=0:
			byte_values=TB*1024*1024*1024*1024
			print("terabytes to bytes:",byte_values)
		elif GB!=0:
			byte_values=GB*1024*1024*1024
			print("gigabytes to bytes:",byte_values)

		elif MB!=0:
			byte_values=MB*1024*1024
			print("megabytes to bytes:",byte_values)
if __name__=="__main__":
	m=Memory()
	m.convertTO(TB=m.TB)
	m.convertTO(GB=m.GB)
	m.convertTO(MB=m.MB)