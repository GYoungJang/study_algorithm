def med3(a, b, c):
    if a >= b:
        if b >= c:
            return b
        elif c >= a:
            return a
        else:
            return c
    elif a > c:
        return a
    elif b > c:
        return c
    else:
        return b


med3(1, 10, 2)
