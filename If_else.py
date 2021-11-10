"""
######КОМАНДЫ IF

cars = ['bmw', 'lambo', 'audi', 'mersedes']
for car in cars:
    if car == 'lambo': # если переменная кар равно выбранному элементу то выполняем след дейстеи->
        print(car.upper()) # ->поднимаем все буквы данного ээллемента в верхний регситр
    else:                   # а иначе просто первые буквы элементов в верхний регистр
        print(car.title())

###вариации как можно если и иначе
age = 18
age_1 = 20
if age == 18:
    print('1. TRUE')
else:
    print('1. False')
if age != 19:
    print('2. NOT')
else:
    print('2. False')
if age <= 19:
    print('3. NOT')
else:
    print('3. False')
if age >= 19:
    print('4. NOT')
else:
    print('4. False')
if age > 19:
    print('5. NOT')
else:
    print('5. False')
if age < 19:
    print('6. NOT')
else:
    print('6. False')
if (age_1>age) and (age<age_1):
    print("7. YES")
else:
    print('7. False')


######ПРОВЕРКА ВХОЖДЕНИЙ ЗНАЧЕНИЙ В СПИСОК
fructs = ['apple', 'banana', 'kivi']
if 'onion' in fructs: # проверяет если данный продукт в списке если есть то выводим да, иначе нет
    print('Yes')
else:
    print('Not')


######ПРОВЕРКА ОТСУТСВИЯ ЗНАЧЕНИЯ В СПИСКЕ
fructs = ['apple', 'banana', 'kivi']
luk = 'onion'
if luk not in fructs:
    print(luk.title() + ' в данном списке нет!')
else:
    print(luk.title + "есть в данном списке!")


    ######ЦЕПОЧКИ IF-ELIF-ELSE
age = 17
if age < 6:
    print("Вы проходите бесплатно! Для посителей меньше 6 лет бесплатно!")
elif age<17:  # elif выполняетя в случае если первая проверка протерпела крах
    print("Для школьников цена составляет 100 руб!")
elif age<18:  # elif выполняетя в случае если первая проверка протерпела крах
    print("Для подростков цена составляет 140 руб!")
else:  # else можно опускать в некоторых случаях, например для проверки условий сверху, работают ли они корректно
    print("Всем кому за 18 цена 180руб")
"""
