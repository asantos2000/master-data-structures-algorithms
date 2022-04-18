def quick_sort(lst):
    if len(lst) <= 1:
        return lst
    else:
        pivot = lst[0]
        less = [i for i in lst[1:] if i <= pivot]
        greater = [i for i in lst[1:] if i > pivot]
        return quick_sort(less) + [pivot] + quick_sort(greater)

if __name__ == '__main__':
    print(quick_sort([54,26,93,17,77,31,44,55,20]))