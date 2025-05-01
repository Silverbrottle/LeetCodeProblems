def maxSubArray(nums):
    """
    Find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.
    :param nums: List[int]
    :return: int
    """
    #Using Kadane's algorithm
    # Time complexity: O(n)
    # Space complexity: O(1)
    # Initialize max_sum and current_sum to the first element
    # of the array starting from the second element
    # Iterate through the array and update current_sum
    # and max_sum accordingly
    max_sum = nums[0]
    current_sum = nums[0]

    for i in range(1, len(nums)):
        current_sum = max(nums[i], current_sum + nums[i])
        max_sum = max(max_sum, current_sum)

    return max_sum

if __name__=='__main__':
    print(maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))  # Output: 6
    # Output: 6
    # Explanation: [4,-1,2,1] has the largest sum = 6.