def loops():
    myseq = ["Austin","New York","Denver","Miami","Atlanta"]
    mysta = ["TX", "NY", "CO", "FL", "GA"]

    for x in myseq:
        print(x)
        if x == "Denver":
            break
    
    for x in myseq:
        if x =="Miami":
            continue
        print(x)

    z = 1
    while z < 10:
        z += 1
        if z == 4:
            break
        print(z)        
            

if __name__=='__main__':
    loops()