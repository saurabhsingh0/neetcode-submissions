class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        ans = []
        for i in range(len(nums)):
            rem = target - nums[i]
            if rem in seen:
                ans.append(seen[rem])
                ans.append(i)
                break
            seen[nums[i]] = i
        return ans