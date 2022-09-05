print('### 1 ###')

def func_1(a, b = 6):
    dob = a * b
    print(dob)
func_1(int(input('enter number: ')))

print('### 2 ###')

def func_2(a, b, c):
    '''triangle area function'''
    p_triangle = (a + b + c) / 2
    S_triangle = (p_triangle * (p_triangle - a)
                  * (p_triangle - b)
                  * (p_triangle - c))**0.5
    print(int(S_triangle))
func_2( int(input('Enter 1 side: ')),
        int(input('Enter 2 side: ')),
        int(input('Enter 3 side: ')))

print('### 3 ###')

def calculate(number_1, number_2, sign):
    result = 0
    if sign == '+':
        result = number_1 + number_2
        print(result)
    elif sign == '-':
        result = number_1 - number_2
        print(result)
    elif sign == '*':
        result = number_1 * number_2
        print(result)
    elif sign == '/':
        result = number_1 / number_2
        print(result)
    else:
        print('Error!')
calculate(int(input('Enter first number: ')),
          int(input('Enter second number: ')),
          str(input('Enter sign: ')))
