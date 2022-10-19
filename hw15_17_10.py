print('With .format and curly braces {}')
print('Anna has {} apples and {} peaches.'.format(1, 2))

print('By passing index numbers into the curly braces.')
print('Anna has {0} apples and {1} peaches.'.format(1, 2))

print('By using keyword arguments into the curly braces.')
print('Anna has {number_of_apples} apples'
      ' and {number_of_peaches} peaches.'
      .format(number_of_apples='1',
              number_of_peaches='2'))
print('With indicators of field size')
print('Anna has {0:5d} apples and {1:3d} peaches.'.format(1, 2))

print('With f-strings and variables')
number_of_apples = 1
number_of_peaches = 2
print(f'Anna has {number_of_apples} apples'
      f' and {number_of_peaches} peaches.')

print('With % operator')
print('Anna has %s apples and'
      ' %s peaches.' % (number_of_apples,
                        number_of_peaches))

print('With variable substitutions by name')
dict_ = {
    'apples': 1,
    'peaches': 2,
}

print(f"Anna has {dict_['apples']} apples and {dict_['peaches']} peaches.")

print("Convert (1) to list comprehension")
list_compreh = [num ** 2 if num % 2 == 1 else num ** 4 for num in range(10)]
print(list_compreh)

print("Convert (2) to regular for with if-else")
list_comprehension = []
for num in range(10):
    if num % 2 == 0:
        list_comprehension.append(num // 2)
    else:
        list_comprehension.append(num * 10)
print(list_comprehension)

print("Convert (3) to dict comprehension.")
dict_compreh1 = {num: num ** 2 for num in range(1, 11) if num % 2 == 1}
print(dict_compreh1)

print("Convert (4) to dict comprehension.")
dict_compreh2 = {num: num ** 2 if num % 2 == 1 else num // 0.5 for num in range(1, 11)}
print(dict_compreh2)

print("Convert (5) to regular for with if.")
dict_comreh3 = {}
for x in range(10):
    if x ** 3 % 4 == 0:
        dict_comreh3[x] = x ** 3
print(dict_comreh3)

print("Convert (6) to regular for with if-else.")
dict_comreh4 = {}
for x in range(10):
    if x ** 3 % 4 == 0:
        dict_comreh4[x] = x ** 3
    else:
        dict_comreh4[x] = x
print(dict_comreh4)


