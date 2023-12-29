def binary_search(arr, target):
    """ Binary Search. """
    low, high = 0, len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1

if __name__ == "__main__":
    example_list = list(range(1, 200, 12))
    print(example_list)
    print(binary_search(example_list, 193))