def longestConsecutive(nums):
        numSet=set(nums)
        longest=0

        for n in numSet:
            # check if its the start of a sequence
            if( n-1) not in numSet:
                length=0
                while (n+length) in numSet:
                    length+=1
                longest=max(length,longest)
        return longest


print(longestConsecutive([100,4,200,1,3,2]))