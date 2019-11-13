def solution(p):
    # p는 balanced
    answer = ''
    return correct(p)


def correct(w):
    if w == '':
        return w

    u, v = _split(w)

    if iscorrect(u):
        return u + correct(v)
    else:
        res = '(' + correct(v) + ')'
        u = u[1:-1]
        for idx in u:
            if idx == '(':
                res += ')'
            else:
                res += '('
        return res


def _split(w):
    left = 0
    right = 0
    for idx in range(len(w)):
        if w[idx] == '(':
            left += 1
        else:
            right += 1
        if left == right:
            return w[:idx + 1], w[idx + 1:]
    return w, ""


def iscorrect(u):
    stack = list()
    for idx in u:
        if idx == '(':
            stack.append(1)
        else:
            if stack:
                stack.pop()
            else:
                return False
    return True