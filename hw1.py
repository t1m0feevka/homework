integer = 1 #1
print(type(integer), ' - тип змінної integer') #1.1

float = 1.1 #2
print(type(float), ' - тип змінної float') #2.1

print(id(integer),' - місце розташування змінної integer',id(float), ' - місце розташування змінної float') #3

print("True, False, if, elif, else, break, while", ' - зарезервовані слова в Python')#4
#5
side = 5
P_square = side * 4
print(P_square, ' - периметр квадрата в задачі №5')
#6
side1 = 4
side2 = 4
side3 = 4
P_triangle = side1 + side2 + side3
print(P_triangle, ' - периметр трикутника в задачі №6')
p_triangle = (side1 + side2 + side3)/2
S_triangle = int((p_triangle*(p_triangle-side1)*(p_triangle-side2)*(p_triangle-side3))**0.5)
print(S_triangle, ' - площа трикутника в задачі №6')
#7
print(6//5, ' - Приклад ділення націло')
#8
print(7%5, ' - Приклад остачі від ділення')
#9
latters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
print(latters[0], ' - Перша літера ', latters[-1], ' - Остання літера')
print(latters[::4], ' - Кожна четверта літера')
