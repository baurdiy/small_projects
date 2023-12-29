def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key


if __name__ == "__main__":
    example_list = [45, 23, 53, 1, 0, 53, 98, 13]
    print(example_list)
    insertion_sort(example_list)
    print(example_list)