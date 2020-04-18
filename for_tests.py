x = input('Please, input your phone number: ')
while x.isdigit()== False:
    print('Please, use digits only!')
    x = input('Please, input your phone number: ')
if len(x)!= 10:
    print('Your number should contain 10 digits only!')
    x = input('Please, input your phone number: ')
else:
    print('Thank you!')

    # x = input('Please, input your phone number: ')
    # while True:
    #     if x.isdigit()== False:
    #     print('Please, use digits only!')
    #     x = input('Please, input your phone number: ')
    # else:
    #     continue
    #     len(x)!= 10
    #     print('Your number should contain 10 digits only!')
    #     x = input('Please, input your phone number: ')
    # else:
    #     print('Thank you!')

    # while  True:
    #   number = ...
    # if number correct:
    #   continue
    # else
    #    print
    #    recomendation
    #   continue

    # while True:
    #     x = input('Please input your number: ')
    #     if x.isdigit == True:
    #         continue
    #     else:
    #         print('Please, use digits only!')
    #         x = input('Please input your number: ')

    # while 1:
    # 	s = input("Введите номер телефона( для выхода введите break): ")
    # 	if s == 'break':
    # 		break
    # 	elif s.isdigit() == True and len(s) == 10:
    # 		print(f'Вы ввели такой номер телeфона - {s}')
    # 	elif s.isdigit() == True and (len(s) != 10):
    # 		print('Номер телефона состоит из 10 цифр. Не переживайте, можете повторить еще раз =) У вас все получится. just do it')
    # 	elif s.isdigit() == False:
    # 		print('Номер состоит только из цифр. Не переживайте, можете повторить еще раз =) У вас все получится. just do it')

    while True:
        number = input("Please, enter your number: ")
        if (number.isdigit()) and len(number) == 10:
            print("Congratulations! Your number has been received.")
            break
        elif (number.isalpha()):
            print("Please, use only numeral characters. Try again.")
        elif (int(number) != 10):
            print("You have entered less or more than 10 numeral characters. Try again.")