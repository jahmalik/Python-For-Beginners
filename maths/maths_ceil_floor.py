def maths_ceil_floor():
    
    import math as mt

    # Get the ceil and floor values of a given number
    x = 64.75

    # Print ceil value of x
    cl_value = mt.ceil(x)
    print(f'The ceil value of {x} is {cl_value}')

    # Print floor value of x
    fl_value = mt.floor(x)
    print(f'The floor value of {x} is {fl_value}')

if __name__=='__main__':
    maths_ceil_floor()