# big O -> O(n^2)
def brute_force(list, target):
    for value1 in list:
        for value2 in list:
            if value1 + value2 == target:
                return True
    return False

list = [1, 2, 3, 6, 4, 7, 5, 9]
target = 16
print("\nBrute force:")
print(brute_force(list, target))