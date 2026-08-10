class Solution {
    Map<Integer, Integer> memo;
    public int rob(int[] nums) {
        memo = new HashMap<>();
        return robHelper(nums, nums.length-1);      
    }

    public int robHelper(int[] nums, int i){
        if(i < 0) return 0;
        if (i == 0) return nums[0];
        if (memo.containsKey(i)) return memo.get(i);

        int val = Math.max(robHelper(nums, i-2)+nums[i], robHelper(nums, i-1));
        memo.put(i, val);
        return val;
    }

}
