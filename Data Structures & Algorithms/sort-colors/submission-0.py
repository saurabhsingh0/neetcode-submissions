class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        left, right, current = 0,len(nums)-1,0

        while current <= right:
            if nums[current] == 0:
                t = nums[current]
                nums[current] = nums[left]
                nums[left] = t
                left += 1
                current += 1 
                continue
            elif nums[current] == 2:
                t = nums[current]
                nums[current] = nums[right]
                nums[right] = t
                right -= 1
            else:
                current += 1
        
        