def loops_while_loop():

    # What is loop ? 
    # An action performs over and over, often with the variations in details each time
    # the mechanism thats meet this need is called a loop

    # Simple While loop
    x = 1
    while x < 11:
        print(x)
        x += 1
        # x=x+1 We can use this also but should be replaced with above line

    
    # BREAK
    # While loop with break statement
    y = 1
    while y < 7:
        print(y)
        if y==5:
            break
        y += 1

    
    # CONTINUE
    # With the continue statement we can stop the current iteration, 
    # and continue with the next
    z = 1
    while z < 10:
        z += 1
        if z == 4:
            continue
        print(z)
    
    
    # ELSE
    # With the else statement we can run a block of code 
    # once when the condition no longer is true:
    k=1
    while k < 5:
        print(k)
        k=k+1
    else:
        print(f'{k} is reached to its maximum limit')




if __name__=='__main__':
    loops_while_loop()