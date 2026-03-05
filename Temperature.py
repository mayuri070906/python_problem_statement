#Overload the method ‘temperature()’ to convert given Kelvin temperature to
#Fahrenheit and Celsius equivalent. Use constructor to initialize the objects.
class Temperature:
	def __init__(self):
		self.K=int(input("Enter temperature in kelvin:"))
	def temperature(self,f=0,c=0):
		if f!=0:
			fahrenheit=(self.K-273.15)*1.8+32
			print(f"Kelvin temperature to fahrenheit:{fahrenheit}F")
		else:
			celsius=self.K-273.15
			print(f"Kelvin temperature to celsius:{celsius}C")
if __name__=="__main__":
	t=Temperature()
	t.temperature(f=1)
	t.temperature(c=1)
	
		
