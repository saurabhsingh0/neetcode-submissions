class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        
        def lcs(text1, text2, m, n):
            if m==0 or n ==0:
                return 0
            if text1[m-1] == text2[n-1]:
                return 1 + lcs(text1, text2, m-1, n-1)
            else:
                return max(lcs(text1, text2, m-1, n), lcs(text1, text2, m, n-1))
        
        memo = {}

        def lcs_memoized(text1, text2, m, n):
            if m==0 or n==0:
                return 0
            if (m,n) in memo:
                return memo[(m,n)]
            
            if text1[m-1] == text2[n-1]:
                memo[(m,n)] = 1 + lcs_memoized(text1, text2, m-1, n-1)
            else:
                memo[(m,n)] = max(lcs_memoized(text1, text2, m-1, n), \
                                lcs_memoized(text1, text2, m, n-1))
            
            return memo[(m,n)]
        
        #return lcs(text1, text2, len(text1), len(text2))
        return lcs_memoized(text1, text2, len(text1), len(text2))