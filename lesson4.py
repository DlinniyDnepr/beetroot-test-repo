#Task1
# The greatest number
import random

random_list = []
while len(random_list) <= 10:
    random_list.append(random.randint(0, 100))
    if len(random_list) == 10:
     print(random_list)
     print(max(random_list))


#Task2
random_list1 = []
random_list2 = []
index = 0
while len(random_list1) <= 10:
    random_list1.append(random.randint(0, 10))
    random_list2.append(random.randint(0, 10))
    index += 1
    item = random_list1[index]
    if item in random_list2:
        print(item)