class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]
        n = len(nums)
        dp = [0] * n
        
        dp[0] = nums[0]
        print(nums)
        for i in range(1,len(nums)):
        
            """
            arr = [-2,3]
            dp = [-2,]
            """
            temp = nums[i] + dp[i-1]

            if temp > nums[i]:
                dp[i] = temp
            else:
                dp[i] = nums[i]
                
                
        print(dp)
        return max(dp)
