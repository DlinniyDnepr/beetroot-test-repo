print('Task 1')
"""
Make a program that has some sentence (a string) on input 
and returns a dict containing all unique words as keys 
and the number of occurrences as values. 
1) Создаем переменную-словарь dict_string
2) Создаем переменную string в которую помещается iput
3) цикл for который достает все слова из введеной строки 
и помещает их в словарь как ключи
4) цикл который помещает индексы слов в значения словаря
5) добавляет в словарь ключ и значение с каждой итерацией цикла for
6) Печать списка
"""
dict_string = {}
string = input('Введи сюда какое либо предложение: ').split()
index = 0
for word in string:
    index += 1
    dict_string[word] = index
print(dict_string)

