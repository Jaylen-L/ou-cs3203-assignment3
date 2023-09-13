def sumArray(array):
    result = 0
    for x in array:
        result += x
    return result

def productArray(array):
    result = 0
    for x in array:
        if result == 0:
            result = x
        result *= x
    return result

def reverseArray(array):
    array2 = array.copy()
    temp = 0
    for x in range(int(len(array2)/2)):
        temp = array2[x]
        array2[x] = array2[len(array2) - (1 + x)]
        array2[len(array2) - (1 + x)] = temp
    return array2



def main():
    numbers = [1, 2, 3, 4, 5]

    print("The sum is:")
    print(sumArray(numbers))

    print("The product is:")
    print(productArray(numbers))

    print("The reverse is:")
    print(reverseArray(numbers))

if __name__ == "__main__":
    main()
