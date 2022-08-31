def merge_sort(arr):
    if len(arr) == 1:
        return arr

    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]

    return merge(merge_sort(left), merge_sort(right))


def merge(left, right):
    combined = []

    # Ok so this works since the arrays are already sorted.
    l_index = 0
    r_index = 0
    while l_index < len(left) and r_index < len(right):
        if left[l_index] < right[r_index]:
            combined.append(left[l_index])
            l_index += 1
        else:
            combined.append(right[r_index])
            r_index += 1

    # One of them is finished, so we just add the remaining one to combined.
    combined = combined + left[l_index:] + right[r_index:]

    return combined


arr = [5, 24, 2, 16, 4, 4, 28, 14, 18, 17, 0]
print(merge_sort(arr))
