#Task1

while True:
    inp = input('Type anything: ')
    x = inp.strip()    #добавил функцию strip которая убирает все пробелы
    if len(x) >= 2:
        print(x[0:2] + x[-2:])
    else:                       #использую else
        len(x) < 2
        print('Empty String')

#Task 2
#The valid phone number program.

while True:
        x = input('Please, input your phone number: ')
        if x ==('stop'):
            break
        elif x.isdigit() == True and len(x) == 10:
            print('Thank you! Wanna try again? if not, print "stop"')
        elif x.isdigit() == False:
            print('Please, use digits only!')
        elif len(x)!= 10:
            print('Your number should contain 10 digits only!')

#Task3

#The name check.

name = 'artem'
while True:
    inp_name = input('Please, input your name: ')
    if inp_name.lower() == name:
        print('Yes! this name is correct! You won!')
        break
    else:
        print('Sorry, but this name is not valid, try again please!')