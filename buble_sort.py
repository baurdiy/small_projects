def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

    
if __name__ == "__main__":
    example_list = [45, 23, 53, 1, 0, 53, 98, 13]
    print(example_list)
    bubble_sort(example_list)
    print(example_list)