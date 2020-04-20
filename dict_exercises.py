'''dictionary exercise 1: Below are the two lists convert it into the dictionary'''
def ex1():
    keys = [1, 2, 3]
    values = ['alefsandler', 'adriana', 'alex']
    newDict = dict(zip(keys, values))
    print(newDict)

'''dictionary exercise 2: Merge following two Python dictionaries into one'''
def ex2():
    dict1 = {'alef': 21, 'adriana': 36, 'bob': 1}
    dict2 = {'somekey': 'somevalue'}
    dict3 = {**dict1, **dict2}
    print(dict3)

'''dictionary exercise 4: Initialize dictionary with default valuesl'''
def ex3():
    sampleDict = {
        "class":{"student":{"name":"Mike","marks":{"physics":70,"history":80}}}}
    print(sampleDict['class']['student']['marks']['history'])

'''dictionary exercise 4: Initialize dictionary with default values'''
def ex4():
    employees = ['Kelly', 'Emma', 'John']
    defaults = {'Application Developer', 8000}
    dictionary = dict.fromkeys(employees, defaults)
    print(dictionaryl)

'''dictionary exercise 5: Create a new dictionary by extracting the following keys from a given dictionary keys = ["name", "salary"]'''
def ex5():
    sampleDict = {"name": "Kelly","age":25,"salary": 8000,"city": "New york"}
    keys = ('name', 'salary')
    newDict = {}
    for k in keys:
        newDict.update({k: sampleDict[k]})
    print(newDict)

'''dictionary exercise 6: Delete set of keys from Python Dictionary'''
def ex6():
    sampleDict = {"name": "Kelly","age":25,"salary": 8000,"city": "New york"}
    remove = ['name', 'salary']
    for i in remove:
        sampleDict.pop(i)

    print(sampleDict)

'''dictionary exercise 7: Check if a value 200 exists in a dictionary'''
def ex7():
    sampleDict = {'a': 100, 'b': 200, 'c': 300}
    if 200 in sampleDict.values():
        print(True)
    else:
        print(False)

'''dictionary exercise 8: Rename key city to location in the following dictionary'''
def ex8():
    sampleDict = {"name": "Kelly","age":25,"salary": 8000,"city": "New york"}
    sampleDict['location'] = sampleDict['city']
    print(sampleDict)


'''dictionary exercise 9: Get the key corresponding to the minimum value from the following dictionary'''
def ex9():
    sampleDict = {'Physics': 82, 'Math': 65, 'History': 75}
             
    print(min(sampleDict, key=sampleDict.get))


'''dictionary exercise 10: Given a Python dictionary, Change Brad’s salary to 8500'''
def ex10():
    sampleDict = {
    'emp1': {'name':'Jhon', 'salary': 7500},
    'emp2': {'name':'Emma', 'salary': 8000},
    'emp3': {'name':'Brad', 'salary': 6500}
    }
    for emp in sampleDict:
        for key in sampleDict[emp]:
            if 'Brad' in sampleDict[emp]['name']:
                sampleDict[emp]['salary'] = 8500
    print(sampleDict)


def main():
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

if __name__ == "__main__":
    main()
