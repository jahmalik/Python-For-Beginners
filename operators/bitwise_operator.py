def operators_bitwise_operator():
    # & 	AND	Sets each bit to 1 if both bits are 1	x & y
    x = 6
    y = 3
    print(x & y)

    # 6 = 0000000000000110
    # 3 = 0000000000000011
    # 2 = 0000000000000010

    # |	OR	Sets each bit to 1 if one of two bits is 1	x | y
    print(x | y)

    # 6 = 0000000000000110
    # 3 = 0000000000000011
    # 7 = 0000000000000111

    # ^	XOR	Sets each bit to 1 if only one of two bits is 1	x ^ y
    print(x ^ y)

    # 6 = 0000000000000110
    # 3 = 0000000000000011
    # 5 = 0000000000000101


if __name__=='__main__':
    operators_bitwise_operator()