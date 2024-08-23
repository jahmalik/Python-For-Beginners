def string_format():

    # Format Price to 2 decimal points
    mystr = "for only {price: .2f} dollars"
    print(mystr.format(price=49))
    # for only  49.00 dollars

    # Name Indexed Formatting
    mystr = "My name is {fname}, I am {age}".format(fname='Usman', age = 6)
    print(mystr)
    #My name is Usman, I am 6

    # Numbered Indexed Formatting
    mystr = "My name is {0}, I am {1}".format('Usman', 6)
    print(mystr)
    #My name is Usman, I am 6

    # empty placeholders Formatting
    mystr = "My name is {}, I am {}".format('Usman', 6)
    print(mystr)
    #My name is Usman, I am 6

    #Use "<" format to left-align the value:
    mystr = "I have {:<8} rabbits.".format(50)
    print(mystr)
    #I have 50       rabbits.

    #Use ">" format to right-align the value:
    mystr = "I have {:>8} rabbits.".format(50)
    print(mystr)
    #I have       50 rabbits.

    #:^ Center aligns the result (within the available space)
    mystr = "I have {:^8} rabbits.".format(50)
    print(mystr)
    #I have    50    rabbits.

    #:= Places the sign to the left most position
    mystr = "The temprature is {:=8} degrees celsius.".format(-5)
    print(mystr)
    #The temprature is -      5 degrees celsius.

    #:+ Use a plus sign to indicate if the result is positive or negative
    mystr = "The temperature is between {:+} and {:+} degrees celsius.".format(-5, 10)
    print(mystr)
    #The temperature is between -5 and +10 degrees celsius.

    # :- Use a minus sign for negative values only
    mystr = "The temperature is between {:-} and {:-} degrees celsius.".format(-5, 10)
    print(mystr)
    #The temperature is between -5 and  10 degrees celsius.

    # : Use a space to insert an extra space before positive numbers (and a minus sign before negative numbers)
    mystr = "The temperature is between {: } and {: } degrees celsius.".format(-5, 10)
    print(mystr)
    #The temperature is between -5 and  10 degrees celsius.

    # :, Use a comma as a thousand separator
    mystr = "I am about {:,} kilometers away from Denver, CO".format(1200)
    print(mystr)
    #I am about 1,200 kilometers away from Denver, CO

    # :_ Use a underscore as a thousand separator
    mystr = "I am about {:_} kilometers away from Denver, CO".format(1100)
    print(mystr)
    #I am about 1_100 kilometers away from Denver, CO

    # :b Use to binary fromat
    mystr = "The binary version of {0} is {0:b}".format(5)
    print(mystr)
    #The binary version of 5 is 101

    # Converts the value into the corresponding unicode character
    mystr = "The unicode character of {0} is {0:c}".format(5)
    print(mystr)
    #The unicode character of 5 is ♣

    # Converts the value into the decimal format
    mystr = "We have {:d} hamsters".format(0b101)
    print(mystr)
    #We have 5 hamsters

    # Scientific format, with a lower case e
    mystr = "We have {:e} hamsters".format(5)
    print(mystr)
    #We have 5.000000e+00 hamsters

    # Scientific format, with a upper case E
    mystr = "We have {:E} hamsters".format(5)
    print(mystr)
    #We have 5.000000E+00 hamsters

    # Fix Point Number Format
    mystr = "We have {:f} hamsters".format(5)
    print(mystr)
    #We have 5.000000 hamsters

    # General Format
    mystr = "We have {:g} hamsters".format(5)
    print(mystr)
    #We have 5 hamsters

    # General Format
    mystr = "We have {:G} hamsters".format(5)
    print(mystr)
    #We have 5 hamsters

    # Use "o" to convert the number into octal format:
    mystr = "The octal version of {0} is {0:o}".format(10)
    print(mystr)
    #The octal version of 10 is 12

    #Use "x" to convert the number into Hex format lowercase:
    mystr = "The hexadecimal version of {0} is {0:x}".format(255)
    print(mystr)
    #The hexadecimal version of 255 is ff

    #Use "X" to convert the number into Hex format uppercase:
    mystr = "The hexadecimal version of {0} is {0:X}".format(255)
    print(mystr)
    #The hexadecimal version of 255 is FF

    #Use "n" Format Number
    mystr = "The number format of {0} is {0:n}".format(12)
    print(mystr)
    #The number format of 12 is 12

    #Use "%" to convert the number into a percentage format:
    mystr = "You scored {:%} ".format(0.25)
    print(mystr)
    #You scored 25.000000%

    #Or, without any decimals:
    mystr = "You scored {:.0%} ".format(0.25)
    print(mystr)
    #You scored 25%

if __name__=='__main__':
        string_format()