class Solution {
    public int subarraySum(int[] nums, int k) {
        // Prefix sum + hashmap approach: count subarrays with sum = k
        Map<Integer, Integer> prefix = new HashMap<>();
        prefix.put(0, 1);
        int sum = 0, count = 0;
        for(int num: nums){
            sum += num;

            // Check if there's a prefix sum that makes current subarray sum = k
            // If sum - k exists, then subarray from that point to current has sum k
            count += prefix.getOrDefault(sum-k, 0);
            prefix.put(sum, prefix.getOrDefault(sum, 0) + 1);
        }

        return count;

    }
}