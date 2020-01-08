#classmethods and staticmethods

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

	#working with the class	instead of the instance
	@classmethod
	def set_raise_amt(cls, amount):
		cls.raise_amt = amount

	#alternative constructor
	@classmethod
	def from_string(cls,emp_str):
		first,last,pay = emp_str.split('-')
		return cls(first,last,pay) 

	#if day its Saturday or Sunday
	@staticmethod
	def is_workday(day):
		if day.weekday() == 5 or day.weekday() == 6:
			return False
		return True


emp_1 = Employee('John','Bary',1000)
emp_2 = Employee('Mike','Jason',3500)

import datetime
my_date = datetime.date(2019,1,6)

print('Is it a work day?')
print(Employee.is_workday(my_date))

#emp_str_1 = 'John-Doe-9999'
#emp_str_2 = 'Steve-Smith-10000'
#emp_str_3 = 'Jane-Doe-9999'

#new_emp_1 = Employee.from_string(emp_str_1)

#print(new_emp_1.email)
#print(new_emp_1.pay)

