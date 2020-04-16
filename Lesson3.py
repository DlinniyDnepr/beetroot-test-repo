#Task1

x = input('Type anything: ')
if len(x) > 1:
    print(x[0:2] + x[-2] + x[-1])
if len(x) < 2:
    print('empty string')

#Task 2
#The valid phone number program.

x = input('Please, input your phone number: ')
if x.isdigit()== False:
    print('Please, use digits only!')
if len(x)!= 10:
    print('Your number should contain 10 digits only!')
else:
    print('Thank you!')
#Интересно как создать петлю чтобы после показа
#ошибки можно было вводить значение снова

#Task3

#The name check.

name = 'artem'
inp_name = input('Please, input your name: ')
if inp_name.lower() == name:
    print('True')
else:
    print('False')