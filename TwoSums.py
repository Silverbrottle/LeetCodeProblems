def twoSum(nums, target):
        hashMap={}
        for i in range(0,len(nums)):
            remainder=target-nums[i]
            print(nums[i],remainder)
            if remainder in hashMap:
                  return [hashMap[remainder],i]
            hashMap[nums[i]]=i
            print("After check:",hashMap)
                
print(twoSum([3,2,4],6))