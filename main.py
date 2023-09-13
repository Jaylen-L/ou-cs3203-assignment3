numbers = [1, 10, -4, 0]

def sumArray(array):
    result = 0
    for x in array:
        result += x
    return result

print("The sum is:")
print(sumArray(numbers))