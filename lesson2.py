from sys import intern

print(5 // 5) #// - Целочисленное деление, / - деление
print(type(5)) # int - intelligence - тип данных целого числа
print(5 % 5) # % - Остаток от деления (четное или не четное число)
print(5 ** 5) # ** - Возведение в степень
print(type(0.2)) # float - тип данных с десятичными дробями
                 # Числа это не изменяемый тип данных
print('Hello world')
print(type("Hello World")) # str - string строка. Всегда в кавычках одинарных или двойных
print("Hello 'World'")
print('hello,' + 'world!')            #concatenate  - сложение строк
print(type(True), type(False)) # Boolean - проверка данных
print(10 < 9, 5 < 6)
print(1,2,3,4, 'Hello, world!', 6 >4)
print(5 == 5) # == - Я утверждаю что эти числа равны
print(5 != 5) # != - Я утверждаю что числа не равны
print(5 != 5 and 5 < 10) # and - строгий апператор (Важно чтобы и левая и правая часть была правдой)
print(5 != 5 or 5 < 10) # or - Не строгий оператор (Только одно из выражений может быть правдой)
print(type(int("123.456"))) # Можно принудительно изменить тип данных прописав нужный тип