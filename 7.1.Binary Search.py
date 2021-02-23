Lists = [96, 102, 122, 307, 324, 476, 477, 478, 809, 834]
Number = 122


def find_value(lst, n):  # O(log)n - because if list size doubles, only one step will be added to our soft
    lower = 0
    upper = len(lst) - 1
    while lower <= upper:
        mid = (lower + upper) // 2

        if lst[mid] == n:
            print('Value is here: ', lst[mid])
            return True
        else:
            if n > lst[mid]:
                lower = mid + 1
            else:
                upper = mid - 1
    print('False')


find_value(Lists, Number)
