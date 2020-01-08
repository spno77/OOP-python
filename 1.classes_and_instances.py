
#initial example

class Employee:
	
	def __init__(self,first,last,pay):
		self.first = first
		self.last = last
		self.pay = pay
		self.email = first + '.' + last + '@company.com'

	def fullname(self):
		return '{} {}'.format(self.first,self.last)


emp_1 = Employee('John','Bary',1000)
emp_2 = Employee('Mike','Jason',3500)

#print(emp_1)
#print(emp_2)

print('printing the emails:')
print(emp_1.email)
print(emp_2.email)

print('---------------------')

print('print the fullnames:')
print(emp_1.fullname())
print(emp_2.fullname())
