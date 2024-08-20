def basic_example():
    # Print a string
    print(' Hello World, Lets Work together to build great future ') 

    # variable declaration on a single line
    mystr,myint,myfloat,mynewstr = 'Global Peace', 2030, 25.75, 'United States'

    # String Concatenation 
    print(mystr + ' ' + mynewstr, end=' | ')
    print(myint, end=' | ')
    print(myfloat, end=' | ')

    # Print String type Variable 
    print(mystr, end=' | ')

    # Print Int type Variable
    print(myint, end=' | ')

    # Print Float type variable
    print(myfloat, end=' | ')

if __name__ == '__main__':
    basic_example()

    