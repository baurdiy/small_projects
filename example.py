def liner_serarch(arr, target):
    """ Perform liner search in the given list for the target value. """
    for i in range(len(arr)):
        if arr[i] == target:
            return i 
    return -1 


if __name__ == "__main__":
    example_list = list(range(1, 200, 4))
    print(example_list)
    print(liner_serarch(example_list, 197))