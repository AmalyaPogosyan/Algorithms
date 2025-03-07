def bubble_sort(ls, reversed = False):
    for i in range(len(ls)):
        changed = False
        for j in range(len(ls) - i - 1):
            if ls[j] > ls[j + 1] and not reversed or ls[j] < ls[j + 1] and reversed:
                ls[j], ls[j + 1] = ls[j + 1], ls[j]
                changed = True
        if not changed:
            return ls
    return ls


ls = [1, 4, -5, 6, -7, 8, -60, 12, 0]
print(bubble_sort(ls, True))