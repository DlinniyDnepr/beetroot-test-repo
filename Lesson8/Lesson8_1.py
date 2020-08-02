
def oops():
	list = [1,2,3,4]
	print(list[5])



try:
	oops()
		# list = [1,2,3,4]
		# print(list[5])

except IndexError:
	print('Sorry, no such Index in a list =)')
	
	