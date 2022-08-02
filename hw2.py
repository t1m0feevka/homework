#1
a = 5
print(f'{a}')
#2
c = [6]
c.append(7)
print(f'{c}')
#3
side1 = 33
side2 = 55
side3 = 44
p = (side1 + side2 + side3)/2
S = int((p*(p-side1)*(p-side2)*(p-side3))**0.5)
print(f'Площа заданого трикутника = {S}')