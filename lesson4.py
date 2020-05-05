print('Task1')
# The greatest number
import random

random_list = []
while len(random_list) <= 10:
    random_list.append(random.randint(0, 101))
    if len(random_list) == 10:
     print('Список из 10 рандомных чисел от 0 до 100', random_list)
     print('Самое большое число в списке, это ', max(random_list))


print('\nTask2')
"""
1 создать рандом список1
2создать рандом список 2
3 сравнить их через Set and set
"""

random_list1 = []
random_list2 = []
while len(random_list1) <= 10:
    random_list1.append(random.randint(0, 10))
    if len(random_list1) == 10:
     print('Первый рандомный список', random_list1)
     break

while len(random_list2) <= 10:
    random_list2.append(random.randint(0, 10))
    if len(random_list2) == 10:
     print('Второй рандомный список', random_list2)

itog = list(set(random_list1) & set(random_list2))
print('Итоговый список включающий совпадающие числа ', itog)

print('\nTask3')

"""
1) Составить список включающий все целые числа от 0 до 100
2) найти все целые числа которые делятся на 7 но не делятся на 5
3) создать список в который эти числа сохранить
4) Распечатать этот список
"""
output_list = []
main_list = list(range(0, 101))
print(f'Это список из всех целых чисел от 0 до 100 \n{main_list}')
for index in main_list:
 if index%7 == 0 and index%5 != 0:
  output_list.append(index)
print(f'\nА это список из целыйх чисел которые делятся на 7 но не делятся на 5  {output_list}')

