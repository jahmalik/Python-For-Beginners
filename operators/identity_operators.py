def number_identity_operators():
    # is 	Returns True if both variables are the same object	x is y
    x = ['apple', 'banana'] # stored in a memory location of 000000001 different object
    y = ['apple', 'banana'] # stored in a memory location of 000000002 different object
    # You can see both objects are stored in a different memory location, so x is not y
    z = x

    print(x is z) # true

    print(x is y) # false

    print(x==y) # true

    # the main difference between == and is the same object and storaage in a memory location

    print(x is not z)

    print(x is not y)

    print(x != y)

if __name__=='__main__':
    number_identity_operators()
    