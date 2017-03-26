def euclide(a, b):
    # a et b sont deux entiers naturels non nuls
    # a >= b
    r = a%b # r est le reste de la division entière de a par b
    while r != 0:
        a = b
        b = r
        r = a%b
    return b


if __name__ == '__main__':
    print(pgcd(1, 1))
    print(pgcd(2, 2))
    print(pgcd(3, 2))
    print(pgcd(4, 2))
    print(pgcd(1071, 1029))
