class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = 0
        for num in nums:
            total += num
        if total%2 != 0:
            return False
        total = total//2
        return self.subset_sum(nums, total, len(nums))


    def subset_sum(self, nums:List[int], sum, index) -> bool:
        if index == 0:
            return False
        if sum == 0:
            return True
        if  nums[index-1] <= sum:
            return self.subset_sum(nums, sum-nums[index-1], index-1) or \
             self.subset_sum(nums, sum, index-1)
        else:
             return self.subset_sum(nums, sum, index-1)