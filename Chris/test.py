## Teaching tool for people who haven't messed with Python 



### Let's create a Test class with initial creation of a number, a string, and a list of nums
class Test: 
	def __init__(self, numbers, strings, lists):
		self.numbers = numbers
		self.strings = strings 
		self.lists = lists 


	# getters 
	def getNumbers(self): 
		return self.numbers 

	def getStrings(self): 
		return self.strings 

	def lists(self): 
		return self.lists

	# setters 
	def modifyNumbers(self, n):
		self.numbers = n 


t = Test(5, "hi", [1,2,3,4,5]) 

print(t.getNumbers())
print(t.getStrings())
print(t.lists)

t.modifyNumbers(1900)
print(t.getNumbers())


def square(x):
	return x * x 


assert square(5) == 25 

assert square(6) == 36 

assert square(11) == 121