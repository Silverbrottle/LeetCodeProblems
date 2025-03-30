def threeSum(nums):
    res=[]
    nums.sort()
    print(nums)
    for i,a in enumerate(nums):
        if i>0 and a == nums[i-1]:
            continue
        l,r=i+1,len(nums)-1
        print("Current Number: ",a,", l: ",l,", r: ",r)
        while l<r:
            threeSum=a+nums[l]+nums[r]
            print(a,"+",nums[l],"+",nums[r],"=",threeSum)
            if threeSum>0:
                r-=1
                print("r reduced to: ",r)
                print("l: ",l,", r: ",r)
            elif threeSum<0:
                l+=1
                print("l increased to: ",l)
                print("l: ",l,", r: ",r)
            else:
                res.append([a,nums[l],nums[r]])
                print("Result added: ",res)
                l+=1
                print("l increased to: ",l)
                print("l: ",l,", r: ",r)
                print("Checking if : ",nums[l],"==",nums[l-1]," and ",l," < ",r)
                while (nums[l]==nums[l-1] and l<r):
                    l+=1    
                    print("l increased to: ",l)
                    print("l: ",l,", r: ",r)
    return res

print(threeSum([-1,0,1,2,-1,-4]))