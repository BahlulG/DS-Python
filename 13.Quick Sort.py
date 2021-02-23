def QuickSort(array, start, end):
    if start < end:
        pivot_index = Partition(array, start, end)
        QuickSort(array, start, pivot_index - 1)
        QuickSort(array, pivot_index + 1, end)


def Partition(array, start, end):
    pivot = array[end]
    pivot_index = start

    for i in range(start, end):
        if array[i] <= pivot:
            array[i], array[pivot_index] = array[pivot_index], array[i]
            pivot_index += 1

    array[end], array[pivot_index] = array[pivot_index], array[end]

    return pivot_index


lst = [5, 2, 3, 14, 65, 7, 38, 11, 5, 4]
print('Array before QuickSort: ', lst)
QuickSort(lst, 0, len(lst) - 1)
print('Array after QuickSort: ', lst)
