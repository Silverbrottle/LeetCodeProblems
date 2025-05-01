# Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest product and return its product.
# The problem is similar to the maximum subarray sum problem, but instead of summing the elements, we are multiplying them.
# Modified kadane's algorithm is used to solve this problem.
# The algorithm keeps track of the maximum product and minimum product at each position in the array.
def maxProduct(nums):
    minProduct=maxProduct=result=nums[0]
    for i in range(1,len(nums)):
        num=nums[i]
        if num<0:
            minProduct,maxProduct=maxProduct,minProduct

        maxProduct=max(num,maxProduct*num)
        minProduct=min(num,minProduct*num)
        result=max(result,maxProduct)

    return result

if __name__=='__main__':
    print(maxProduct([2,3,-2,4]))  # Output: 6
    # Output: 6
    # Explanation: [2,3] has the largest product 6.
    print(maxProduct([-2,0,-1]))  # Output: 0
    # Output: 0
    # Explanation: The result cannot be 2, because we need to form a subarray.
    # Note: The product of an empty subarray is 1 by definition.
    print(maxProduct([-2,3,-4]))  # Output: 24
    # Output: 24
    # Explanation: The result is 24, because we choose the subarray [-2,3,-4] which has the largest product.
    # Note: The product of an empty subarray is 1 by definition.
    print(maxProduct([0,2]))  # Output: 2
    # Output: 2
    # Explanation: The result is 2, because we choose the subarray [2] which has the largest product.
    # Note: The product of an empty subarray is 1 by definition.