x = input('Please, input your phone number: ')
while x.isdigit()== False:
    print('Please, use digits only!')
    x = input('Please, input your phone number: ')
if len(x)!= 10:
    print('Your number should contain 10 digits only!')
    x = input('Please, input your phone number: ')
else:
    print('Thank you!')