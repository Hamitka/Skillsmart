def BiggerGreater(s: str):
    if len(set(s)) <= 1: return ''
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

    permutation(list(s))
    lstPermutation = [i for i in lstPermutation if i > s]
    return (min(lstPermutation))


# print(BiggerGreater('fff'))
# print(BiggerGreater(''))
# print(BiggerGreater('нклм'))
# print(BiggerGreater('вибк'))
# print(BiggerGreater('вкиб'))
