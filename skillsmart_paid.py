def BalancedParentheses(N: int):
    assert N > 0
    lstPermutation = []

    def permutation(a, k=0):
        nonlocal lstPermutation
        if k == len(a):
            lstPermutation += [''.join(a)]
        else:
            for i in range(k, len(a)):
                a[k], a[i] = a[i], a[k]
                permutation(a, k + 1)
                a[k], a[i] = a[i], a[k]

    permutation(['(', ')'] * N)

    def bkt(s: str):
        open, close = 0, 0
        for i in s:
            if '(' in i:
                open += 1
            elif ')' in i:
                close += 1
            if open-close <0: return False
        if open-close == 0: return True
        else: return False

    lst_bkt = [i for i in set(lstPermutation) if bkt(i)]
    return ' '.join(lst_bkt, )


# print(BalancedParentheses(4))
