
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


class Developer(Employee):
	raise_ammount = 1.10

	def __init__(self,first,last,pay,prog_lang):
		super().__init__(first,last,pay)
		self.prog_lang = prog_lang

class Manager(Employee):

	def __init__(self,first,last,pay,employees=None):
		super().__init__(first,last,pay)
		if employees is None:
			self.employees = []
		else:
			self.employees = employees

	def add_emp(self,emp):
		if emp not in self.employees:
			self.employees.append(emp)

	def remove_emp(self,emp):
		if emp in self.employees:
			self.employees.remove(emp)

	def print_emps(self):
		for emp in self.employees:
			print('-->',emp.fullname())


#instances of Employee class
dev_1 = Developer('John','Bary',1000,'Python')
dev_2 = Developer('Mike','Jason',3500,'Java')

mgr_1 = Manager('Sue','Smith',10000,[dev_1])

print(mgr_1.email)

mgr_1.add_emp(dev_2)
mgr_1.remove_emp(dev_1)

mgr_1.print_emps()

#print(help(Developer))

#print(dev_1.email)
#print(dev_1.prog_lang)

#print(dev_1.pay)
#dev_1.apply_raise()
#print(dev_1.pay)