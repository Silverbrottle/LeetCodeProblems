def alphaNum(c):
    return ((ord('A')<=ord(c)<=ord('Z')) or
        (ord('a')<=ord(c)<=ord('z')) or
        (ord('0')<=ord(c)<=ord('9')))
            
def isPalindrome(s):
    l,r=0,len(s)-1
    while l<r:
        #print("Outer While loop:",s[l],s[r])
        while l<r and not alphaNum(s[l]):
            l+=1
        while r>l and not alphaNum(s[r]):
            r-=1
        #print("After Inner While loop:",s[l],s[r])
        if s[l].lower()!=s[r].lower():
            return False
        l,r=l+1,r-1
    
    return True

print(isPalindrome("A man, a plan, a canal: Panama"))