class Solution {
    public void sortColors(int[] nums) {
        int left = 0, right = nums.length-1, current = 0;
        while(current <= right) {
            if (nums[current] == 0){
                int temp = nums[current];
                nums[current] = nums[left];
                nums[left] = temp;
                left++;
                current++;
                continue;
            }
            else if (nums[current] == 2){
                int temp = nums[current];
                nums[current] = nums[right];
                nums[right] = temp;
                right --;
            }
            else {
                current++;
            }
        }
    }
}