def productExceptSelf(nums):
        res=[1]*len(nums)
        #prefix output
        prefix=1
        for i in range(0,len(nums)):
            res[i]=prefix
            prefix*=nums[i]
        #postfix output
        postfix=1
        for i in range(len(nums)-1,-1,-1):
            res[i]=res[i]*postfix
            postfix*=nums[i]
        return res

print(productExceptSelf([1,2,3,4]))