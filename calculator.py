
#while 1:

while True:
    name = input('Привет, меня зовут Калькулятор, а тебя? -> ')
    if  name.isalpha() == False:
        #name = input('Привет, меня зовут Калькулятор, а тебя? -> ')
        print('Имя может состоять только из букв, попробуй снова!')
    elif name.isalpha() == True:
        #else:
        name = name.capitalize()
        print(f'Привет {name}, а давай ка посчитаем!')


        print(f' {name}, выбери операцию которую хотел бы произвести: \nесли хочешь выполнить СЛОЖЕНИЕ введи +'
              f'\nесли хочешь выполнить ВЫЧИТАНИЕ введи -\nесли хочешь выполнить УМНОЖЕНИЕ введи *'
              f'\nесли хочешь выполнить ДЕЛЕНИЕ введи /\nесли хочешь увидеть результат от ЦЕЛОЧИСЛЕННОГО ДЕЛЕНИЯ введи //'
              f'\nесли хочешь увидеть остаток от деления одного числа на другое введи % ' )