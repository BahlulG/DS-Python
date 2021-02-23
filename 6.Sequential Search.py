def SeqSearch(lists, item):
    pos = 0
    found = False

    while pos < len(lists) and not found:
        if lists[pos] == item:
            found = True
        else:
            pos += 1

    return found


list1 = [1, 4, 12, 20]

print(SeqSearch(list1, 5))
