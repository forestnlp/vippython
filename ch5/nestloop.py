

for i in range(1,4):
    for k in range(1,6):
        print('*',end='\t')
    print()




for i in range(1,10):
    for k in range(1,i+1):
        print(i,'*',k,'=',i*k,end='\t')
    print()


for i in range(5):
    for k in range(1,11):
        if(k%2==0):
            #break
            continue
        print(k,end='\t')
    print()