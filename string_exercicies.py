'''Given a string of odd length greater 7, return a string made of the middle three 
chars of a given String'''
def ex1():
	s1 = str(input("Enter a string of odd length greater 7: "))
	s2 = s1[(len(s1)//2 - 1): (len(s1)//2 + 2)]
	print("Orginal String is %s" %(s1))
	print("Middle three chars are %s" %(s2))


'''Given 2 strings, s1 and s2, create a new string by appending s2 in the 
middle of s1'''
def ex2():
	s1 = str(input("Enter a string: "))
	s2 = str(input("Enter a string: "))
	print("Appending s2 in the middle of s1:")
	s3 = s1[0: len(s1)//2] + s2 + s1[len(s1)//2 : len(s1)]
	print(s3)


'''Given 2 strings, s1, and s2 return a new string made of the first, middle and 
last char each input string'''
def ex3():
	s1 = str(input("Enter a string: "))
	s2 = str(input("Enter a string: "))
	s3 = s1[0] + s2[0] + s1[len(s1)//2] + s2[len(s2)//2] + s1[len(s1)-1] + s2[len(s2)-1]
	print("The new string is", s3)


'''arrange String characters such that lowercase letters should come first'''
def ex4():
	s1 = str(input("Enter a string: "))
	upper = []
	lower = []
	for c in s1:
		if c.islower():
			lower.append(c)
		elif c.isupper():
			upper.append(c)
	newString = ''.join(lower + upper)
	print("The new string arranged is", newString)


'''Given a string input Count all lower case, upper case, digits, and special symbols'''
def ex5():
	string = str(input("Enter a string: "))
	upper, lower, digits, specials = 0, 0, 0, 0
	for c in string:
		if c.isupper():
			upper+=1
		elif c.islower():
			lower+=1
		elif c.isdigit():
			digits+=1
		else:
			specials+=1
	print("uppers = ", upper)
	print("lowers = ", lower)
	print("digits = ", digits)
	print("specials = ", specials)


'''Given two strings, s1 and s2, create a mixed String

Note: create a third-string made of the first char of the last char of b, the second 
char of the second last char of b, and so on. Any leftover chars go at the end of 
the result.'''
def ex6():
	s1 = str(input("Enter a string: "))
	s2 = str(input("Enter a string: "))
	sAux = []
	i, j = 0, len(s2)-1
	cont = True
	while cont:
		if i < len(s1):
			sAux.append(s1[i])
			i+=1
		if j >= 0:
			sAux.append(s2[j])
			j-=1
		if i >= len(s1) and j < 0:
			cont = False

	newString = ''.join(sAux)
	print("The new string is", newString)


'''String characters balance Test

We’ll say that a String s1 and s2 is balanced if all the chars in the string1 are 
there in s2. characters position doesn’t matter.'''
def ex7():
	s1 = str(input("Enter a string: "))
	s2 = str(input("Enter a string: "))
	result = True

	for c in s2:
		if c not in s1:
			result = False
			break

	print(result)


'''Find all occurrences of “USA” in given string ignoring the case'''
def ex8():
	s1 = str(input("Enter a string: "))
	sAux = []
	for c in s1:
		sAux.append(c.upper())

	newString = ''.join(sAux)

	print("USA appears %d times in %s" %(newString.count("USA"), s1))


'''Given a string, return the sum and average of the digits that appear in the 
string, ignoring all other characters'''
def ex9():
	s1 = str(input("Enter a string: "))
	sum_digits, qt_digits, i = 0, 0, 0
	s1Aux = []
	for c in s1:
		s1Aux.append(c)

	while i < len(s1Aux):
		digits, sum_Aux = [], 0
		if s1Aux[i].isdigit():
			while i < len(s1Aux):
				if not s1Aux[i].isdigit():
					break
				else:
					digits.append(int(s1Aux[i]))
					i += 1
			for j in range(len(digits)):
				sum_Aux *= 10
				sum_Aux += digits[j]	
			qt_digits += 1
			sum_digits += sum_Aux
		else:
			i += 1
	print("The sum of the digits is %d and the average is %f" %(sum_digits, sum_digits/qt_digits))


'''Given an input string, count occurrences of all characters within a string'''
def ex10():
	s1 = str(input("Enter a string: "))
	alreadyExists = []
	for c in s1:
		if alreadyExists.count(c) == 0:
			print("%s: %d times" %(c, s1.count(c)))
			alreadyExists.append(c)
		else:
			continue


#ex1()
#ex2()
#ex3()
#ex4()
#ex5()
#ex6()
#ex7()
#ex8()
#ex9()
#ex10()