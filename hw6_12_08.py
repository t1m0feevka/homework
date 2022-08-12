####### 1 #######
number = int(input('Enter a number: '))
if number > 0:
    print('Number is positive!')
elif number < 0:
    print('Number is negative!')
else:
    print('0 - is neither positive nor negative!')

###### 2 #######
x = int(input('Enter coordinates x: '))
y = int(input('Enter coordinates y: '))
if x > 0 and y > 0:
    print('first quarter')
elif x < 0 and y > 0:
    print('second quarter')
elif x < 0 and y < 0:
    print('third quarter')
elif x > 0 and y < 0:
    print('fourth quarter')
else:
    print('0 - cannot be a coordinate')

####### 3 #######
number1 = float(input('Enter a number 1: '))
number2 = float(input('Enter a number 2: '))
if number1 > number2:
    print('number1 is greater than number2')
elif number2 > number1:
    print('number2 is greater than number1')
else:
    print('number1 = number2')

