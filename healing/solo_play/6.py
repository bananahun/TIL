def KFC(x):
    if x == 6:
        return

    print(x, end = ' ')
    KFC(x + 1)
    print(x, end = ' ')

KFC(0)


def KFC(X):
    if X == 3:
        return
    KFC(X + 1)
    KFC(X + 1)

KFC(0)
