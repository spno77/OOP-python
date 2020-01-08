#class variables 

class Employee:
	num_of_emps = 0
	raise_ammount = 1.04

	def __init__(self,first,last,pay):
		self.first = first
		self.last = last
		self.pay = pay
		self.email = first + '.' + last + '@company.com'

		Employee.num_of_emps += 1

	def fullname(self):
		return '{} {}'.format(self.first,self.last)

	def apply_raise(self):
		self.pay = int(self.pay * self.raise_ammount)

emp_1 = Employee('John','Bary',1000)
emp_2 = Employee('Mike','Jason',3500)

print('num of employees: {}'.format(Employee.num_of_emps))

#print(Employee.__dict__)

#print(emp_1.pay)
#emp_1.apply_raise()
#print(emp_1.pay)



