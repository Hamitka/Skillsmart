def Football(F:list, N:int) -> bool:
    if len(F)<=1: return False
    dict_orig = {i: val for i, val in enumerate(F)}
    dict_sort = {i: val for i, val in sorted(dict_orig.items(), key=lambda x: x[1])}
    lst_diff = [list(dict_orig.keys())[i] - list(dict_sort.keys())[i] for i in range(len(F))]

    def check_replace() -> bool:
        if len(set(lst_diff)) == 3:
            return True
        return False

    def check_reverse() -> bool:
        lst_index_change = [i for i, val in enumerate(lst_diff) if val !=0]
        min_reverse, max_reverse = min(lst_index_change), max(lst_index_change)
        lst_reverse = list(map(int, (list(map(str, F[:min_reverse])) + list(map(str, F[min_reverse:max_reverse+1][::-1])) + list(map(str, F[max_reverse+1:])))))
        if lst_reverse == sorted(F):
            return True
        return False
    if check_replace() or check_reverse():
        return True
    return False


# print(Football([1]))
# print(Football([3, 2]))
# print(Football([1, 3, 2]))
# print(Football([1, 7, 5, 3, 9]))
# print(Football([9, 5, 3, 7, 1]))
# print(Football([1, 4, 3, 2, 5]))
# print(Football([1, 5, 4, 3, 2, 6]))
# print(Football([1, 5, 4, 3, 2, 7, 6]))