def conditions_control_if_else():
    # Python Conditions and If statements
    a = 20
    b = 5
    if a > b:
        print(f'{a} is greater than {b}')

    # The elif keyword is Python's way of saying "if 
    # the previous conditions were not true, then try this condition".

    if a < b:
        print(f'{a} is less than {b}')
    elif a > b:
        print(f'{a} is greater than {b}')

    # The else keyword catches anything which isn't caught by the preceding conditions
    if a < b:
        print(f'{a} is less than {b}')
    elif a == b:
        print(f'{a} is equal to {b}')
    else:
        print(f'{a} is greater than {b}')

    # Short Hand If
    if a > b: print(f'{a} is greater than {b}')
    
    # Short Hand If ... Else
    print(f'{a} is less than {b}') if a < b else print(f'{a} is greater than {b}')

    # AND
    # The and keyword is a logical operator, 
    # and is used to combine conditional statements:
    # Let's test if Test if c is greater than d, AND if e is greater than d:
    c = 200
    d = 33
    e = 500
    if c > d and e > d:
        print(f'{c} is greater than {d} and {e} is also greater than {d}')

    # OR
    # The or keyword is a logical operator, 
    # and is used to combine conditional statements:
    # Test if c is greater than d, OR if c is greater than e:
    if c > d or c > e:
        print("At least one of the condition is TRUE")

    # NOT
    #The not keyword is a logical operator, 
    # and is used to reverse the result of the conditional statement:
    # Test if c is NOT greater than d:
    e=31
    f=325
    if not e > f:
        print(f'{e} is not greater than {f}')

    # Nested If Statements
    # You can have if statements inside if statements, 
    # this is called nested if statements.
    y = 81
    if y > 45:
        print(f'{y} is not greater')
        if y >75:
            print(f'{y} is still not greater')
        else:
            print('3rd statement')

    # The pass statement
    # If statement cannot be empty, that's why we use pass keyword in case if there is not content
    # under the if statement
    if a > b:
        pass
    

if __name__=='__main__':
    conditions_control_if_else()
