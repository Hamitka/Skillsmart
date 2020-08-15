def BalancedParentheses(N: int):
    lst_out = []

    def bkt(S='', left=0, right=0):
        if len(S) == 2 * N:
            lst_out.append(S)
            return
        if left < N:
            bkt(S + '(', left + 1, right)
        if right < left:
            bkt(S + ')', left, right + 1)

    bkt()
    return ' '.join(lst_out)

# print(type(BalancedParentheses(4)))
# print((BalancedParentheses(10)))
# print((BalancedParentheses(4)))
# # print ([i for i in ['()()()()', '()(())()', '(()()())', '(()())()', '()()(())', '(())()()', '(()(()))', '(())(())', '()(()())', '((())())', '()((()))', '((()))()', '((()()))', '(((())))'] if i not in BalancedParentheses(4)])
# print((BalancedParentheses(3)))
# print((BalancedParentheses(2)))
# print((BalancedParentheses(1)))
