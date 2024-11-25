def romanToInt(str):
        length=len(str)
        chr={'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        rev_str=[str[length-1-i] for i in range(0,length)]
        sum1=0
        prev_val=0
        for i in range(0,length):
            val_from_chr=int(chr[rev_str[i]])
            if(val_from_chr<prev_val):
                sum1=sum1-val_from_chr
            else:
                sum1=sum1+val_from_chr
            prev_val=val_from_chr


        return sum1
        
io=input("Roman Number: ")
print(romanToInt(io))