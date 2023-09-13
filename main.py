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

def main():
    numbers = [1,2,3,4]

    print("The sum is:")
    print(sumArray(numbers))

    print("The product is:")
    print(productArray(numbers))

if __name__ == "__main__":
    main()