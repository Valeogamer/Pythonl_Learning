"""
###ВВЕДЕНИЕ В PYTHON
print("hi")
message = "Hello"
print(message)
message = "Helloxxx"
print(message) 
name = "valentine"
print(name.title()) #title преобразует первый символ каждого слова в строке в вверхний регистр
print(name.upper())
print(name.lower())
first_name = "valentin"
last_name = "zhilin"
full_name = first_name + " " + last_name
print("Hello, my name is " + full_name.title() + "!")
"""

#print("Languages:\n\t\tPython\n\t\t\tC\n\t\t\t\tJavaScript")#t-табуляция n - новая строка
#slovo = "hi   "
#print(slovo.rstrip())# rstrip - удаление пропусков справа lstrip - слева strip - с обоих концов

"""
print(2+2)
x = 2
y = 7
print(x+y,'\n', x-y,'\n', x*y,'\n', x/y)
print("Мне "+ str(y) + " лет!") # str-преобразование в строчный вид из числовой
import this - заповеди прогера
"""

"""
###СПИСКИ
cifr = ['one', 'two', 'three', 'four']
print(cifr)# вызов всего списка
print(cifr[0]) #вызов выбранного элемента со списка  
print(cifr[0].title()) # вызов выбранного и некое действо над ним
print(cifr[-1]) #вызов последнего элемента списка -2 -  предпоследний и -3 и тд сзади
print("У меня есть" + "\t" + cifr[-2] + " яблок!")


### упражнения
friends_name = ['Artem', 'Kirill', 'Daniil', 'Zheka']
print("Hi my dear friends " + friends_name[0] + "!")
print("Hi my dear friends " + friends_name[-3] + "!")
lan = ['C++', 'C', 'Xyz', 'Python']
lan[2] = 'C#' #- замена элемента в списке
print(lan)
lan.append('javascript') #append - добавление нового элемента в конец списка
print(lan)
lan.insert(2,'css') # insert - добавление элемента в указанное место в списке
print(lan)
del lan[1] # del - удаление из списка выбранного элемента
print(lan)
popped_lan = lan.pop() # pop - метод удаляющий последний элемент из списка
print(popped_lan)
print(lan)
print("В списке последним оказался " + popped_lan)
first_lan = lan.pop(0) # достаем произвольный элемент
print("В списке первым оказался " + first_lan)
lan.remove("Python") # remove - удаление выбранного элемента 
print(lan)


###СПИСКИ-СОРТИРОВКА
auto = ['mersedes', 'bmw', 'audi', 'tesla']
print(auto)
auto.sort() # sort сортировка в алфавит порядке, в порядке возрастания
print(auto)
auto.sort(reverse=True) # в обратном порядке
print(auto)
print(sorted(auto)) # sorted - временная сортировка 
print(auto)
auto = ['mersedes', 'bmw', 'audi', 'tesla']
auto.reverse() # читаемость в обратном порядке
print(auto)
aa = len(auto) # len - определение длиный списка
print(aa)


#РАБОТА СО СПИСКАМИ
car = ['lada', 'volvo', 'audi', 'opel']
#print(car)


#######цкил
#for car in car: #вывод всего списка с помощью цикла for каждый элемент в новой строке
    #print(car)


#########цикл
#for car in car:
#    print(car.title() + ".corp") # можем с помощью цикла для каждого элемента сопоставить предложения


###ЦИКЛЫ С ЧИСЛАМИ
#for value in range(1,5): # range - построение числовых последовательностей
#    print(value)


###СОЗДАНИЕ ЧИСЛОВГО СПИСКА
numbers = list(range(1,6)) #list - создание списка; range - построение числовой последователности в заданном порядке
print(numbers)

num = list(range(2,11,2)) #построение четных числе, последовательность начинаем на 2 и заканчиваем на 11 и перескок 2
print(num)

squares = []   # создаем список
for value in range(1,11): # цикл где валуе числа ранже диапазон
    square = value**2  # присваиваем square значение валуе и возводим в степень **2
    squares.append(square) # добавляем в список squares с помощью метода append значения полученные в square
print(squares) # выводим на терминал

schisl_posled = [1,2,3,46,754,24,131,24]
minn = min(schisl_posled)
maxx = max(schisl_posled)
summ = sum(schisl_posled)
print("Mиинимум данной последовательности=" + str(minn) + "\nМаксимум данной последовательности=" + str(maxx) + "\nСумма данной последовательности=" + str(summ))

squr = [valuee**2 for valuee in range(1,11)] # более короткий метод построить список с квадратным числом
print(squr)


####CРЕЗ
players = ['one', 'two', 'three', 'four', 'five']
print(players[0:3])#вывели нужный нам диапазон элементов от 0 до 3
print(players[1:4])#вывели нужный нам диапазон элементов от 1 до 4
print(players[:4])#вывели нужный нам диапазон элементов автоматом от нуля до 4
print(players[2:])#вывели нужный нам диапазон элементов пропускаем первые два
print(players[-3:])#вывели нужный нам диапазон элементов последние три
copy = players[:] #копирует список :
print(copy)


###Кортежи - неизменяеммый список
healse = (100, 50)
print(healse[0])
print(healse[1])
#Перебор значений в кортеже
for value in healse:
    print(value)
#Элементы кортежа не могут изменяться но вы можете присвоить новое значение переменной а которой храниться кортеж
healse = (150, 30)
print(healse[0])
print(healse[1])
"""


