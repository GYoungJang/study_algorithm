def med3(a, b, c):
    if a >= b:
        if b >= c:
            return b
        elif c >= a:
            return a
        else:
            return c
    elif b < c:
        return b
    elif c < a:
        return a
    else:
        return c


med3(1, 10, 2)
med3(3, 10, 2)
med3(3, 1, 2)
med3(3, 2, 1)
med3(2, 1, 3)
med3(1, 2, 3)
med3(2, 2, 3)
med3(2, 2, 1)
med3(2, 3, 3)
med3(4, 3, 3)
med3(2, 3, 2)
med3(2, 1, 2)
med3(2, 2, 2)
