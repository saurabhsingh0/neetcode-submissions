class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i,j = 0, len(numbers)-1
        while i<j:
            currSum = numbers[i] + numbers[j]

            if currSum > target:
                j -= 1
            elif currSum < target:
                i+=1
            else:
                return [i+1, j+1]
            
        return []