def rdfsa(arr):
    print(arr)
    counter=0
    prev=0
    for i in arr:
        if prev==i and counter<=2:
            counter+=1
        elif prev!=i:
            counter=0
        else:
            for j in range(arr.index(i),len(arr)):
                






print(rdfsa([0,0,1,1,1,1,2,2,3,3]))


