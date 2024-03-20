def suma(a, b):
    return a+b

a=2
b=1

print("Hola mundo")

def binary_search(arr, x):
    low = 0
    high = len(arr) - 1
    mid = 0
    while low <= high:
        mid = (high + low) // 2
        if arr[mid] < x:
            low = mid + 1
        elif arr[mid] > x:
            high = mid - 1
        else:
            return mid
    return -1

def main():
    print("Binary Search")
    print("Enter the list of numbers: ")
    input_string = input()
    user_list = input_string.split()
    user_list = [int(i) for i in user_list]
    print("Enter the number to be searched: ")
    number = int(input())
    result = binary_search(user_list, number)
    if result != -1:
        print("Element is present at index", str(result))
    else:
        print("Element is not present in the list")