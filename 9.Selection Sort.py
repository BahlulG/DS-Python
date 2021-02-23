Lists = [324, 476, 477, 478, 809, 834, 96, 102, 122, 307]


def Selection_Sort(lst):  # O(n2) - because of nested loop
    for i in range(len(lst)):
        min_value = i
        for j in range(i + 1, len(lst)):
            if lst[j] < lst[min_value]:
                min_value = j

        if i != min_value:
            lst[i], lst[min_value] = lst[min_value], lst[i]

    print(lst)


Selection_Sort(Lists)
