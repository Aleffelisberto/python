class Employee(object):
	
	num_of_emps = 0
	raise_amt = 1.04

	def __init__(self, first, last, pay):
		self.first = first
		self.last = last
		self.email = first + '.' + last + '@email.com'
		self.pay = pay

		Employee.num_of_emps += 1

	def fullname(self):
		return '{} {}'.format(self.first, self.last)

	def apply_raise(self):
		self.pay = int(self.pay * self.raise_amt)

	@classmethod
	def set_raise_amt(cls, amount):
		cls.raise_amt = amount

	@classmethod
	def from_string(cls, emp_str):
		first, last, pay = emp_str.split('-')
		return cls(first, last, int(pay))
	
	@staticmethod
	def isRich(salary):
		if salary >= 55000:
			return True
		return False

	def __repr__(self):
		return 'Employee({}, {}, {})'.format(self.first, self.last, self.pay)	

	def __str__(self):
		return '{} - {}'.format(self.fullname(), self.email)

	def __add__(self, other):
		return self.pay + other.pay

	def __len__(self):
		return len(self.fullname())

emp_1 = Employee('Corey', 'Schafer', 50000)
emp_2 = Employee('Test', 'Employee', 60000)

emp_str1 = 'John-Doe-70000'
emp_str2 = 'Steve-Smith-30000'

new_emp1 = Employee.from_string(emp_str1)

print(emp_1)
print(emp_1.__repr__())
print(len(emp_1))
print('The total pay is', emp_1 + emp_2)
