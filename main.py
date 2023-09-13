numbers = [1, 2, 3, 4]

def sumArray(array):
    result = 0
    for x in array:
        result += x
    return result

print("The sum is:")
print(sumArray(numbers))

def productArray(array):
    result = 0
    for x in array:
        if result == 0:
            result = x
        result *= x
    return result

print("The product is:")
print(productArray(numbers))