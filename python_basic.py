#https://pynative.com/python-basic-exercise-for-beginners/

'''Given a range of first 10 numbers, Iterate from start number to the end number 
and print the sum of the current number and previous number'''
def ex2():
	previous = 0
	for i in range(0, 10, 1):
		print("Current number", i, "Previous Number", previous, "Sum", (previous + i))
		previous = i


'''Accept string from a user and display only those characters which are 
present at an even index number.'''
def ex3():
	str = input("Enter String ")
	print("Original is", str)
	print("Printing only even index chars")
	for i in range(len(str)):
		if(i % 2 == 0):
			print("index[%d] is %c" %(i, str[i]))


'''Given a string and an integer number n, remove characters from a string starting 
from zero up to n and return a new string'''
def ex4():
	str = input("Enter String: ")
	N = int(input("Enter a delimiter to remove the N first characters: "))
	if(N > len(str)):
		print('Invalid input!')
	else:
		str1 = str[N:len(str)]
		print("New string is", str1)


'''Given a list of numbers, return True if first and last number of a list is same'''
def ex5():
	n = int(input("Length of list (n > 0): "))
	thislist = []
	for i in range(n):
		number = int(input('array number: '))
		thislist.append(number)

	if(thislist[0] == thislist[n-1]):
		print("result is true. ", thislist[0], "is equal to", thislist[0])
	else:
		print("result is false. ", thislist[0], "isn't equal to", thislist[0])


'''Given a list of numbers, Iterate it and print only those numbers which are 
divisible of 5'''
def ex6():
	n = int(input("Length of list (n > 0): "))
	thislist = []
	for i in range(n):
		number = int(input())
		thislist.append(number)

	print("Divisible of 5 in a list")
	print("Given list is", thislist)
	print("Divisible numbers to 5 are")
	for i in range(n):
		if(thislist[i] % 5 == 0):
			print(thislist[i])


'''Return the total count of string “Emma” appears in the given string'''
def ex7():
	string = input("Enter something: ")
	print("Emma appeared", (string.count("Emma")), "times")


''' Print the following pattern

1 
2 2 
3 3 3 
4 4 4 4 
5 5 5 5 5'''
def ex8():
	for i in range(1, 6):
		for j in range(i):
			print(i, end =" ")
		print()


'''Reverse a given number and return true if it is the same as the original number'''
def ex9():
	number = int(input("Digite some positive number: "))
	nAux = number;
	nTransf = 0;
	while nAux != 0:
		nTransf *= 10
		nTransf += nAux % 10
		nAux = (nAux - (nAux % 10)) // 10

	print("Is palindrome" if (nTransf == number) else "Isn't palindrome")


'''Given a two list of numbers create a new list such that new list should contain 
only odd numbers from the first list and even numbers from the second list'''
def ex10():
	n = int(input("Length of list1 (n > 0): "))
	n2 = int(input("Length of list1 (n > 0): "))
	thislist = []
	thislist2 = []
	thislist3 = []
	for i in range(n):
		number = int(input())
		thislist.append(number)
		if number % 2 == 1 and number not in thislist3:
			thislist3.append(number)
		
	for i in range(n2):
		number = int(input())
		thislist2.append(number)
		if number % 2 == 0 and number not in thislist3:
			thislist3.append(number)

	print("list1:", thislist)
	print("list2:", thislist2)
	print("Result list3:", thislist3)


#ex2()
#ex3()
#ex4()
#ex5()
#ex6()
#ex7()
#ex8()
#ex9()
#ex10()