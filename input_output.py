import fileinput
import os

''' Display “My Name Is James” as “My**Name**Is**James” using output formatting of a print() function'''
def ex2():
    print("My", "Name", "Is", "James", sep="**")


'''Convert decimal number to octal using print() output formatting'''
def ex3():
    num = int(input("Enter a decimal integer: "))
    print(oct(num))


'''Display float number with 2 decimal places using print()'''
def ex4():
    num = float(input("Enter a float: "))
    print("%.2f" % num)


'''Accept list of 5 float numbers as a input from user'''
def ex5():
    print("Digit 5 float numbers to create a list")
    flList = []
    for i in range(5):
        elem = float(input())
        flList.append(elem)

    print(flList)


'''write all file content into new file by skiping line 5 from following file'''
def ex6():
    count = 1
    input_file = open('input.txt', 'r')
    output_file = open('output.txt', 'w')
    for line in input_file:
        if count != 5: 
            output_file.write(line)
            count += 1
        else:
            count += 1
            continue

    input_file.close()
    output_file.close()


'''write all file content into new file by skiping line 5 from following file'''
def ex7():
    s1, s2, s3 = input().split()
    print(s1, s2, s3)


'''You have following data display it using string.format() method as per 
the following condition'''
def ex8():
    quantity = 3
    totalMoney = 1000
    price = 450
    print("I have {1} dollars so I can buy {0} cards for {2:.2f} dollars".format(quantity, totalMoney, price))


'''How to check file is empty or not'''
def ex9():
    file_input = open('file.txt', 'r')
    # st_size tells about the size of the file in bytes.
    if os.path.exists('file_input') or os.stat('file_input').st_size == 0:
        print("The file is empty")
    else:
        print("There's some content in the file")

    # another way
    with open('file_input', 'r') as fl:
        char = fl.read(1)
        if not char:
            print("The file is empty")
        else:
            print("There's some content in the file")


'''Read line number 4 from the following file'''
def ex10():
    with open('file.txt', 'r') as file_input:
        lines = file_input.readlines()
        if len(lines) >= 4:
            print(lines[3], end="")
        else:
            print("Length less than 4")


#ex2()
#ex3()
#ex4()
#ex4()
#ex5()
#ex6()
#ex7()
#ex8()
#ex9()
#ex10()