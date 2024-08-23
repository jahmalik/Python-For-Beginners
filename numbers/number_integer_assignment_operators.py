def number_assignment_operators():
    num1 = 32
    num2 = 2
    # =	x = 5	x = 5
    print(num1)

    # +=	x += 3	x = x + 3
    num2 +=3
    print(num2)

    # -=	x -= 3	x = x - 3
    num1 -=12
    print(num1)

    # *=	x *= 3	x = x * 3
    num2 *=6
    print(num2)

    # /=	x /= 3	x = x / 3
    num1 /=4
    print(num1)

    # %=	x %= 3	x = x % 3
    num1 %=4
    print(num1)

    # //=	x //= 3	x = x // 3
    num1 //=4
    print(num1)

    # **=	x **= 3	x = x ** 3
    num1 **=3
    print(num1)

    # &=	x &= 3	x = x & 3
    num2 &=2
    print(num2)

if __name__=='__main__':
    number_assignment_operators()