dict_animals = {
    1: 'cat',
    2: 'dog',
    3: 'tiger',
    4: 'pig',
    5: 'horse',
}                          # 1.1
del dict_animals[5] # 1.2
dict_animals[5] = 'chicken' # 1.3
print(dict_animals, ' - dictionary of animals') # 1.4
print('--------------')
list_numbers = [1, 2, 3, 4, 5] # 2.1
list_numbers.append(6) # 2.2
print(list_numbers, ' - list of numbers') # 2.3
print('--------------')
tuple_colors = ('rad', 'black', 'white', 'orange', 'blue') # 3.1
print(tuple_colors, ' - tuple of colors') # 3.2
print('--------------')
set_fruits = {'apple', 'banana', 'pear', 'orange', 'lemon'} # 4.1
print(set_fruits, ' - set of fruits') # 4.2
print('--------------')
a = 1 #5
b = 100 #6
if b > a:
    print('Умова виконується!!!, b > a') # 7
if b < a:
    print('Умова не виконується!!!, b > a!') # 8
if b != a:
    print('Умова не виконується!!!, b != a') # 9
print('--------------')
print(max(a, b), ' - larger number') #10
print('--------------')
x = int(input('enter whole number: '))
if x % 2 == 0:
    print('yes, the number is even ')
else:
    print('no, the number is not even') #11
print('--------------')
print(pow(max(list_numbers),2), ' - the largest number in list_number was **2') #12
