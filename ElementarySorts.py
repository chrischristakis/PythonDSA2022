def bubble_sort(arr):
    for end_index in range(len(arr)-1, 0, -1):
        for i in range(0, end_index):
            if arr[i] > arr[i+1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]
    return arr


def selection_sort(arr):
    for i in range(0, len(arr)):
        min = i
        for j in range(i+1, len(arr)):
            if arr[j] < arr[min]:
                min = j
        arr[i], arr[min] = arr[min], arr[i]
    return arr


def insertion_sort(arr):
    for end in range(1, len(arr)):
        base = arr[end]
        i = end-1

        while i >= 0 and base < arr[i]:
            arr[i+1] = arr[i]
            i -= 1

        arr[i+1] = base
    return arr


arr = [5, 24, 2, 16, 4, 4, 28, 14, 18, 17, 0]
print(bubble_sort(arr))
print(selection_sort(arr))
print(insertion_sort(arr))