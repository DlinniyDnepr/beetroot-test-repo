print("Task 3\n")

"""
List comprehension exercise

Use a list comprehension to make a list containing tuples (i, j) 
where `i` goes from 1 to 10 and `j` is corresponding to `i` squared
"""

i = [x for x in range(10)]
#i = (i)
print(i)
j = [x**2 for x in i]
#j = (j)
print(j)
List = [i, j]
print(List)