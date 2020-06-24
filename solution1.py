# Find a pair of numbers which sum equals to a another number
# Using two indexes
def find_target(array, target):
	min = 0
	max = len(array) -1 
	while (min <= max):
		if ( array[min] + array[max] == target ):
			return True
		if ( array[min] + array[max] < target):
			min += 1
		else:
			max -= 1	
	return False

list = [1, 2, 3, 6, 4, 7, 5, 9]
target = 16
print("Using two indexes:")
print(find_target(list, target))