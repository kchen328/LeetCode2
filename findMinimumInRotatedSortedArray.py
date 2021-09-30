class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        def helper(l,r,nums):
            
            if l == r:
                return nums[l]
            
            mid_index = l + (r - l)// 2 
            
            if nums[mid_index] > nums[r]:
                # go to the right
                return helper(mid_index+1,r,nums)
            else:
                # go to the left
                return helper(l,mid_index,nums)
            
        return helper(0,len(nums)-1,nums)
            
            
                
            
        
        
