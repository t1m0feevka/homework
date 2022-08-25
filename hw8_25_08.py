import random
print('---------- 1 ----------')

list1 = [i for i in range(16)]
print(list1)

print('---------- 2 ----------')

list2 = []
list2_ = [list2.append(0) for i in range(10)]
print(list2)

print('---------- 3 ----------')

list3 = [i**2 for i in range(2, 9)]
print(list3)

print('---------- 4 ----------')

list4 = [random.randint(1, 10) for i in range(15)]
print(list4)

