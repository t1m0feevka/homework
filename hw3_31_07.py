list1 = [] #1
list2 = ['winter', 'spring', 'summer'] #2
list2.append('autumn') #2.1
list2.remove('spring') #2.2
list3 = [1, 2, 3, 4, 5] #3
all_list = []
all_list.extend(list1)
all_list.extend(list2)
all_list.extend(list3) #4
list2[1] = 'summer' #5
all_list.pop(-1) #6
list_numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
print(list_numbers[2::2]) #7
list_numbers.reverse()
print(list_numbers) #8
tuple1 = (1, 'cat', True) #9
list2_2 = ['winter', 'spring', 'summer']
tuple2 = tuple(list2_2)
print(tuple2[-1]) #10