def selection_sort(arr):
    for i in range(len(arr)):
        min_index = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]


if __name__ == "__main__":
    example_list = [45, 23, 53, 1, 0, 53, 98, 13]
    print(example_list)
    selection_sort(example_list)
    print(example_list)