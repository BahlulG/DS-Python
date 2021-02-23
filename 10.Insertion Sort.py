Lists = [324, 476, 477, 478, 809, 834, 96, 102, 122, 307]


def insertion_sort(array):
    for index in range(1, len(array)):
        temp_value = array[index]
        position = index - 1
        while position >= 0:
            if array[position] > temp_value:
                array[position + 1] = array[position]
                position = position - 1
            else:
                break
        array[position + 1] = temp_value
    return array


print(insertion_sort(Lists))
