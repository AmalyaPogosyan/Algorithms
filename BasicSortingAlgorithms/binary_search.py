def binary_search_iterative(ls, target):
    start = 0
    end = len(ls) - 1
    while start <= end:
        mid = (start + end) // 2
        if ls[mid] == target:
            return mid
        if target < ls[mid]:
            end = mid - 1
        else:
            start = mid + 1
    return -1

def binary_search_recursive(ls, target, start = 0, end = None):
    if end == None:
        end = len(ls) - 1
    mid = (start + end) // 2
    if start > end:
        return -1
    elif ls[mid] == target:
        return mid
    if ls[mid] > target:
        return binary_search_recursive(ls, target, start, mid - 1)
    else:
        return binary_search_recursive(ls, target, mid + 1, end)
 
ls = [1, 2, 5, 7, 9, 12]   

print(binary_search_recursive(ls, 12)) 