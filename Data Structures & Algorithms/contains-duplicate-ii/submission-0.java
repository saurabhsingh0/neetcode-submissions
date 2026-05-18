class Solution {
    public boolean containsNearbyDuplicate(int[] nums, int k) {
        Set<Integer> set = new HashSet<>();
        for(int i=0,j=0;j<nums.length; j++){
            if(set.contains(nums[j])){
                return true;
            }
            set.add(nums[j]);
            if(j-i == k){
                set.remove(nums[i]);
                i++;
            }
        }
        return false;
    }
}