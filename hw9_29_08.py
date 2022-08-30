print('---------- 1 ----------')

a = []
text = 'Hello world'
for i in text:
    if i == ' ':
        continue
    a.append(i)
print(' '.join(a))

### list compreh 1 ####

a1 = [i for i in text if i != ' ']
print(' '.join(a1))

print('-----------------------')

f = []
e = 0
while e < len(text):
    e += 1
    f.append(text[e-1])
if ' ' in text:
    f.pop(5)
print(' '.join(f))

print('---------- 2 ----------')

k = 0
f = []
while True:
    k += 1
    if k == 5:
        break
    f.append(k)
print(f)

### list compreh 2 ####

list1 = [i for i in range(1, 11) if i < 5]
print(list1)

print('---------- 3 ----------')

l = 0
l1 = []
while l < 10:
    l += 1
    if l == 5:
        continue
    l1.append(l)
print(l1)

### list compreh 3 ####

list2 = [i for i in range(1, 11) if i < 5 or i > 5]
print(list2)

print('---------- 4 ----------')

j = 1
result = 1
number = int(input('Enter number: '))
pow1 = int(input('Enter number of power: '))
while j <= pow1:
    result = result * number
    j += 1
print(result)

## list compreh 4 ####

f = int(input('Enter number: '))
g = int(input('Enter number of power: '))
list3 = [f**g for i in range(1)]
print(list3)

print('---------- 5 ----------')

result = 0
n = int(input('Enter number: '))
for i in range(1, n+1):
    result = result + i / (2 * i + 1)
    print(result)
print(result)

print('---------- 6 ----------')

result1 = 0
for i in range(1, 4):
    for j in range(1, 3):
        result1 = result1 + 1 / (i + j**2)
        print(result1, end='\t')
print(result1)

print('---------- 7 ----------')

def func_sum(a, b):
    c = a + b
    print('Sum = ', c)
func_sum(int(input('Enter first number: ')), int(input('Enter second number: ')))

print('---------- 8 ----------')

def func_args(*args):
    print(args)
func_args('Hello', 1, 2, True, 'you')
