def buildArray(nums):
    return [nums[nums[i]] for i in range(0,len(nums))]

print(buildArray([0,2,1,5,3,4]))