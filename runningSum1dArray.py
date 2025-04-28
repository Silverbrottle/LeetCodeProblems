def runningSum(nums):
    runningSums=[]
    for i in range(0,len(nums)):
        if i==0:
            runningSums.append(nums[i])
        else:
            runningSums.append(runningSums[i-1]+nums[i])
    return runningSums

print(runningSum([1,2,3,4]))