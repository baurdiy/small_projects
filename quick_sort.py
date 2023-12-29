def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    
    pivot = arr[0]
    left = []
    right = []

    for element in arr[1:]:
        if element < pivot:
            left.append(element)
        else:
            right.append(element)

    
    return quick_sort(left) + [pivot] + quick_sort(right)


if __name__ == "__main__":
    arr = [12, 11, 13, 5, 6, 7]
    sorted_arr = quick_sort(arr)
    print(sorted_arr) 



