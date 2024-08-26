def loops_for_loop():

    # What is loop ? 
    # An action performs over and over, often with the variations in details each time
    # the mechanism thats meet this need is called a loop

    # A for loop is used for iterating over a sequence
    contin = ["Asia","America","Africa","Australia","Europe"]
    for x in contin:
        print(x)

    # Looping Through a String
    mystr = "HelloWorld"
    for x in mystr:
        print(x)
    
    # The break Statement
        for x in contin:
            print(x)
            if x =="Africa":
                break
    
    # The continue Statement
        for x in contin:
            if x =="Australia":
                continue
            print(x)

    # The range() Function
        for x in range(6):
            print(x)

    # The range() Function With Start and End Parameter        
        for x in range(3,7):
            print(x)

    # The range() Function with Start and End Parameter and Increment Parameter
        for x in range(2, 25, 5):
            print(x)

    # For Loop With Else Statement
        for x in range(5):
            print(x)
        else:
            print('Loop Concluded')

    # Nested For Loops
    adj = ["red", "big", "tasty"]
    fruits = ["apple", "banana", "cherry"]

    for x in adj:
        for y in fruits:
            print(x, y)

if __name__=='__main__':
    loops_for_loop()