import random
print('---------- 1 ----------')

list1 = [i for i in range(16)]
print(list1)

print('---------- 2 ----------')

list2 = [0 for i in range(10)]
print(list2)

print('---------- 3 ----------')

list3 = [i**2 for i in range(2, 9)]
print(list3)

print('---------- 4 ----------')

list4 = [random.randint(1, 10) for i in range(15)]
print(list4)

print('---------- - ----------')

list_letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
list_numbers = ['1','2','3','4','5','6','7','8','9']
your_password = []
list_all = list_letters + list_numbers
for i in range(6):
    your_password.append(random.choice(list_all))
print(''.join(your_password))