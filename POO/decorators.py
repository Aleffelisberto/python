'''Getters, Setters and Deleters'''
class Employee:

	def __init__(self, first, last):
		self.first = first
		self.last = last
	
	@property
	def email(self):
                return '{}.{}@email.com'.format(self.first, self.last)

	@property
	def fullname(self):
		return '{} {}'.format(self.first, self.last)

	@fullname.setter
	def fullname(self, name):
		first, last = name.split(' ')
		self.first = first
		self.last = last

	@fullname.deleter
	def fullname(self):
		self.first, self.last = None, None

emp1 = Employee('Alefsandler', 'Felisberto')

emp1.fullname = 'Alef Felisberto'

print(emp1.first)
print(emp1.email)
print(emp1.fullname)

del emp1.fullname
