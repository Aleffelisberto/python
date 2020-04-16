'''
Python has the following data types built-in by default, in these categories:
	Text Type: 	str
	Numeric Types: 	int, float, complex
	Sequence Types: 	list, tuple, range
	Mapping Type: 	dict
	Set Types: 	set, frozenset
	Boolean Type: 	bool
	Binary Types: 	bytes, bytearray, memoryview
'''
x = "Hello World" #str 	
x = 20 #int 	
x = 20.5 #float
x = 1j #complex number
x = ["apple", "banana", "grape"] #list
x = ("apple", "banana", "grape") #tuple
x = range(10) #range
x = {"nome" : "Alefsandler", "age" : 36} #dict
x = {"apple", "banana", "grape"} #set
x = frozenset({"apple", "banana", "grape"}) #frozenset
x = True #bool
x = b"Hello" #byte
x = bytearray(5) #bytearray
x = memoryview(bytes(5))

# construction functions
y = str("Hello World")
y = int(20)
y = float(20.5)
y = complex(1j)
y = list(("apple", "banana", "grape"))
y = tuple(("apple", "banana", "grape"))
y = range(10)
y = dict(name="Alefsandler", age=21)
y = set(("apple", "banana", "grape"))
y = frozenset(("apple", "banana", "grape"))
y = bool(5)
y = bytes(5)
y = bytearray(5)
y = memoryview(bytes(5))