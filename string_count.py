def string_count():
    #Count specific value in a given string
    mystr = "I eat oranges and oranges are my favorite fruit"
    print(mystr.count('oranges'))

    #Search from position 10 to 24:
    print(mystr.count('oranges', 6, 15))


if __name__=='__main__':
    string_count()

