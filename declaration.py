def declair_sinngle_line_variables():

    # declaring all variables on a single line
    mystr,mystr2,mystr3,myint,myfloat  = "E-Commerce", "App", "Jamal Malik", 2023, 1.3

    # printing all variables in a single line
    print (mystr,mystr2,mystr3,myint,myfloat)

    # Concatinating String Variables and Integer by Converting int into string by using str function
    #print("Plugin Name is: " + mystr + " " + mystr2 + " Published Year: " + str(myint) + " Version: " + str(myfloat) )

    # but you can make that line of code even more readable by using a f string
    #rint(f' Newly Built plugin is {mystr} {mystr2} developed by {mystr3}, published in {myint}. Its current version is {myfloat} on wordpress directory.')

    # you can split long strings into multiple shorter ones as follows:
    #print(f' Newly Built plugin is {mystr} {mystr2} developed by {mystr3} published in'
    #  f' {myint}. Its current version is {myfloat} on wordpress directory.')

    if __name__ == '__main__': 
        declair_sinngle_line_variables()