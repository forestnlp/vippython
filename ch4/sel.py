for i in range(1,1000):
    a = input('input a num')

    na = int(a)

    if(na>1000):
        print(na,">1000")
    elif(na<1000):
        print(na,"<1000")
    else:
        print(na,"==1000")