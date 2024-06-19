print("18.06.24")
print(type(5 + 5))
print(5 + 5)
print(5 * 5)
print(5 / 5)
print(5 // 5)
print(1 / 3)
print(1 // 3)
print(5 / 5) # // integer
print(1 / 3) # / float
print(1 % 3) # =1 % остаток от деления
print(4 % 2) # =0 но четное при делении
print(6 % 2) # =0 но нечетное при делении
print(5 % 5) # =0 если остаток от деления на 2 = 0 тогда число четное
print(5 ** 2)
print(type(2.0)) # class float
print(2.0 + 2.0) # результат - такое же число в формате (class) float
print(2 + 1 / 3) # если один float, то результат float

print("Hello World!") # при работе с текстом ставим ковычки в начале и в конце текста
print(type("Hello World!")) # тип str - string
print('"Hello World!"') # ковычки без разницы, если только не хочу отобразить ковычким "Hello World!"
print('Hello' + ' ' + 'World!') # concatenate - сложение слов
print('Hello' + ' World!') # concatenate - пробел
print(1 + 1) # print('1' + 1) TypeError: can only concatenate str (not "int") to str
print('1' + '1') # комп понимает это как текст - внимание!
print(1 + 1)
print(type(True), type(False)) # <class 'bool'> <class 'bool'> boolean
print(5 > 10, 5 < 10)
print(1, 2, 'Hello World', 5 < 10) # запятая разделяет объекты, комп понимает разные типы объектов в одном принте
print(5 <= 5) # знак равно второй
print(5 >= 10) # знак равно второй
print(5 == 5) # равны ли
print(5 != 5) # не равны ли
print(5 != 5 and 5 < 10)
print(5 != 5 or 5 < 10)
print(5 == 5 and 5 < 10) # операторы

print(int('5')) # конвертировали и получили число из текста
print(type(int('5'))) # точно integer
print(type(float('5'))) # читаем с конца: 5.0 тип принт
print(type(bool('5')))