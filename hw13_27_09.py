import random
# 1
s = "Дуже вибачаюсь!, але сьогодні теж не виходить!, виникли певні. проблеми?."
a = s.split()
print(a)git
a = [i.strip('.,!?') for i in a if i != '']
print(a)
for i in a:
    if len(i) == len(set(i)):
        print(i)


# 2
n = int(input('Enter first number(n): '))
m = int(input('Enter second number(m): '))
sum_ = 0
for i in range(n, m+1):
    if i % 2 == 1 and i > 0:
        sum_ += i
print('Sum of odd positive numbers from n to m - ', sum_)

# 3
list_random = [random.randint(1, 100) for i in range(10)]
sum = 0
dob = 1
sered = 0
print(list_random)
for i in list_random:
    sum += i
    dob *= i
    sered = sum / 10
print(sum, '- sum')
print(dob, '- dobytok')
print(sered, '- average value')

# 4
list_random1 = [random.randint(1, 100) for i in range(15)]
print(list_random1)
print(max(list_random1), '- max number')
print(list_random1.count(max(list_random1)), '- count of max number')

# 5


def to_dict(a):
    dict_1 = {
        i: i for i in a
    }
    return dict_1


print(to_dict([1, 2, 3, 4, 5]))

# 6


def more_than_five(a):
    new_list = []
    for i in a:
        if abs(i) > 5:
            new_list.append(i)
    return new_list


print(more_than_five([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, -6, -34]))


