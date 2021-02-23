def BinarySearch(lists, item):  # O(log)n - because if list size doubles, only one step will be added to our soft
    first = 0
    last = len(lists) - 1
    found = False

    while first <= last and not found:
        midpoint = (first + last) // 2
        if lists[midpoint] == item:
            found = True
        else:
            if item < lists[midpoint]:
                last = midpoint - 1
            else:
                first = midpoint + 1

    return found


testlist = [0, 1, 2, 8, 13, 17, 19, 32, 42, ]
print(BinarySearch(testlist, 3))
print(BinarySearch(testlist, 13))
