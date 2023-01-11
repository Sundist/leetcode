class Solution:
    def maxSubArray(self, nums) -> int:
        maxSum = nums[0]
        maxSubSum = nums[0]

        for i in range(1,len(nums)):
            maxSubSum = max(maxSubSum + nums[i], nums[i])
            if maxSum < maxSubSum:
                maxSum = maxSubSum
        return maxSum