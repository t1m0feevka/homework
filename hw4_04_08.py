number = 92145 #1
number_with_dot = 45623.123 #2
text = 'goose' #3
list1 = [number, number_with_dot, text, False] #4
print(list1[1], ' - second element in list') #5
tuple1 = ('one', True, 345345) #6
tuple2 = tuple(list1) #7
dict1 = {
    1: 'June',
    2: 'July',
    3: 'August',
    4: 'Septrmber',
    5: 'October',
}                     #8
dict1[6] = 'November' #9
del dict1[6]
print(dict1.values(), ' - list of dict values') #10
print(dict1.keys(), ' - list of dict keys') #11
print(dict1.items(), ' - list of dict items') #12
numbers = dict(zip([1, 2, 3], ['One', 'Two', 'Three']))
print(numbers, ' - creating dict with lists, keys, values ') #13

#############

a = {
    1: 'One',
    2: 'Two',
    3: 'Tree',
    4: 'Four',
}
set1 = {5, 6, 7, 8}
a_keys = a.keys()
print(a_keys | set1, ' - combining keys from list with sets')
