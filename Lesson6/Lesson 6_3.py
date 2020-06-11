print('Task 3')

'''
A simple calculator.

Create a function called make_operation, 
which takes in a simple arithmetic operator as a first parameter 
(to keep things simple let it only be ‘+’, ‘-’ or ‘*’) 
and an arbitrary number of arguments (only numbers) as the second parameter. 
Then return the sum or product of all the numbers in the arbitrary parameter. 


'''


def make_operation(a, *list_of_nums):
    print(list_of_nums[0])
    
    if a == "+":
        result = 0
        for n in list_of_nums:
            result = result + n
        print("Result is: ", result)

    elif a == "-":
        result = list_of_nums[0]
        for n in list_of_nums:
            result = result - n
        print("Result is: ", result)

    elif a == "*":
        # result = list_of_nums[1]
        for n in list_of_nums:
            result = result * n
        print("Result is: ", result)
    # else:
    #     print('Wrong operation, choose +, - or *'):


make_operation("-", 5, 5, -10, -20)
