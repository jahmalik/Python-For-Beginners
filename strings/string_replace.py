def string_replace():

    #String Replace
    mystr = "python is awesome language to learn and work, python used for ML"
    print(mystr.replace('python','node.js'))

    #no. of occurances to replace - need to pass 3rd parameter of count. -1 replaces all occurance
    print(mystr.replace('python','node.js', -1))

    #replaces only first occurance
    print(mystr.replace('python','node.js', 1))

if __name__=='__main__':
    string_replace()