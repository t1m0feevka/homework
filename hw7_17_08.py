import random
list_numbers = [12, 25, 98, 156, 36, 87]
sum = 0
for i in list_numbers:
    sum += i
print(sum, ' - sum of all numbers in list')

print('----------------------------')

list_names = ['Vladislav', 'Nikita', 'Roma', 'Artem', 'Igor']
for a, b in enumerate(list_names):
    print(f'{a} - index | {list_names[a]} - name')

print('----------------------------')

x = int(input('Enter whole number: '))
for h in range(x):
    h = h**2
    print(h)

print('----------------------------')

for a in range(15, 0, -1):
    print(a)

print('----------------------------')

list_random = []
number_of_elements = int(input('Enter number of random numbers: '))
for i in range(0, number_of_elements):
    list_random.append(random.randint(1, 120))
print(list_random)

print('----------------------------')

email1 = 'yuriiwebblack@gmail.com'
for i in email1:
    if i == '@':
        break
    print(i)

print('----------------------------')

f = []
for i in email1:
    if i == '@':
        continue
    elif i == '.':
        continue
    f.append(i)
print(''.join(f))

print('----------------------------')

a = 1
w = []
while len(w) < 10:
    w.append(a)
    a += 2
print(w)

print('----------------------------')

b = 21
while b != 10:
    b -= 1
    print(b)

print('----------------------------')

list_ = [3, 5, 7] * 4
while 5 in list_:
    list_.remove(5)
print(list_)

print('----------------------------')

x1 = int(input('Enter whole number: '))
while x1 > 0:
    u = x1 % 10
    print(u ** 2)
    x1 = x1 // 10
