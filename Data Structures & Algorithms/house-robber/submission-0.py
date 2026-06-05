class Solution:
    def rob(self, nums: List[int]) -> int:
        memo = {}
        def rob_helper(index):
            if index == 0:
                return 0
            if index == 1:
                return nums[0]
            
            if index in memo:
                return memo[index]
            
            memo[index] = max(rob_helper(index-1), \
                        rob_helper(index-2) + nums[index-1])
            return memo[index]
        
        return rob_helper(len(nums))
            
        