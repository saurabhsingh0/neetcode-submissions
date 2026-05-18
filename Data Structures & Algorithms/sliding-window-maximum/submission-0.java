class Solution {
    public int[] maxSlidingWindow(int[] nums, int k) {
        Deque<Integer> dq = new ArrayDeque<>();
        int[] ans = new int[nums.length-k+1];

        for(int i=0, j=0; j<nums.length; j++){
            if(dq.isEmpty() || dq.getLast() >= nums[j]){
                dq.offerLast(nums[j]);
            }
            else {
                while(!dq.isEmpty() && dq.getLast() < nums[j]){
                    dq.removeLast();
                }
                dq.offerLast(nums[j]);
            }
            if(j-i+1 == k){
                ans[i] = dq.getFirst();
                if(nums[i] == dq.getFirst()){
                    dq.removeFirst();
                }
                i++;
            }

        }
        return ans;
    }
}
