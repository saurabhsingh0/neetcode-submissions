class Solution {
    public int rob(int[] nums) {
        int n = nums.length;
        if (n == 1) return nums[0];
        if (n == 2) return Math.max(nums[0], nums[1]);

        // Case 1: exclude last house -> rob range [0, n-2]
        Map<Integer, Integer> memo1 = new HashMap<>();
        int result1 = robHelper(nums, n - 2, 0, memo1);

        // Case 2: exclude first house -> rob range [1, n-1]
        Map<Integer, Integer> memo2 = new HashMap<>();
        int result2 = robHelper(nums, n - 1, 1, memo2);

        return Math.max(result1, result2);
    }

    public int robHelper(int[] nums, int i, int start,  Map<Integer, Integer> memo) {
        if (i < start) return 0;
        if (memo.containsKey(i)) return memo.get(i);

        int val = Math.max(robHelper(nums, i - 2, start, memo) + nums[i], 
                            robHelper(nums, i - 1, start, memo));

        memo.put(i, val);
        return val;
    }
}
