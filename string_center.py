def string_center():

    #String Center - taking up the space of n characters of a string, Using the letter "X as the padding character
    mystr = "pythonlanguage"
    newstr = mystr.center(5, "X")
    print(newstr)

if __name__=='__main__':
    string_center()