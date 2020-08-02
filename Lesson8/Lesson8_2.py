'''
Write a function that takes in two numbers from the user via input(), 
call the numbers a and b, and then returns the value of squared a divided by b, 
construct a try-except block which raises an exception if the two values given 
by the input function were not numbers, and if value b was zero (cannot divide by zero).
'''
def function():
   
    a = float(input("Please input number "))
    b = float(input("Please input enother number "))
        
    print(a**0.5/b)

while True:
 try:
     function()

 except  ValueError:
    print("You should add a nums only, try again please")  
    continue
 except ZeroDivisionError:
    print("You can not divide by zero! lets try from begining" )
    continue