Lists = [324, 476, 477, 478, 809, 834, 96, 102, 122, 307]


def bubble_sort(lst):  # O(n2) - because of every element compared against all the element inside the list
    unsorted_until_index = len(Lists) - 1
    Sorted = False
    while not Sorted:  # While Sorted is True, while loops circles inside Loop. When Sorted equals to False, while loop Breaks.
        Sorted = True
        for i in range(unsorted_until_index):
            if lst[i] > lst[i + 1]:
                lst[i], lst[i + 1] = lst[i + 1], lst[i]
                Sorted = False
        unsorted_until_index -= 1
    print(lst)


bubble_sort(Lists)
