def binarysearch():
    # binary search

    # input
    n = int(input("Enter the number of elements: "))
    arr = list(map(int, input("Enter the elements: ").split()))
    x = int(input("Enter the element to search: "))
    arr.sort()

    # binary search
    low = 0
    high = n - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] < x:
            low = mid + 1
        elif arr[mid] > x:
            high = mid - 1
        else:
            return mid
    return -1