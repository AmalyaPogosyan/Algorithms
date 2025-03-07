def selection_sort(ls, reversed = False):
    for i in range(len(ls)):
        idx = i
        for j in range(i + 1, len(ls)):
            if (ls[j] < ls[idx] and not reversed) or (ls[j] > ls[idx] and reversed):
                idx = j
        ls[idx], ls[i] = ls[i], ls[idx]
    return ls

ls = [1, 4, -5, 6, -7, 8, -60, 12, 0]
print(selection_sort(ls, True))