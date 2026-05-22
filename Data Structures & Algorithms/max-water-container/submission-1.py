class Solution:
    def maxArea(self, heights: List[int]) -> int:
        i,j, ans = 0, len(heights)-1, 0
        while(i<j) :
            maxHeight = min(heights[i], heights[j])
            ans = max(ans, maxHeight*(j-i))
            if heights[i] < heights[j]:
                i += 1
            else:
                j -= 1
        
        return ans

        