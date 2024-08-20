def string_endswith():
    str = "Pything is awesome language and it is good for ML"
    print(str.endswith('good for ML'))

    print(str.endswith('good for ML', 5, 13))

if __name__=='__main__':
    string_endswith()
