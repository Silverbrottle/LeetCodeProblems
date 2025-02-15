def encode(l1):
    res=""
    for s in l1:
        res+=str(len(s))+"#"+s
    return res

def decode(encstr):
    res,i=[],0
    while i<len(encstr):
        j=i
        while encstr[j]!="#":
            j+=1
        length=int(encstr[i:j])
        res.append(str(encstr[j+1:j+length+1]))
        i=j+1+length
    return res


list1=["lint","code","love","you"]
encstr_g=encode(list1)
print("Encoded string",encstr_g)
print("Decoded string",decode(encstr_g))