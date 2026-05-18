class Solution {
    public int largestRectangleArea(int[] heights) {
        int[] nsr = nextSmallerToRight(heights);
        System.out.println(Arrays.toString(nsr));
        int[] psl = previousSmallerToLeft(heights);
        System.out.println(Arrays.toString(psl));
        int ans = 0;
        for(int i=0; i<heights.length; i++){
            ans = Math.max(ans, heights[i]*(nsr[i]-psl[i]-1));
        }
        return ans;
    }

    static int[] nextSmallerToRight(int[] nums){
        Deque<int[]> stack = new ArrayDeque<>();
        int[] nsr = new int[nums.length];
        for(int i=nums.length-1; i>=0; i--){
            while(!stack.isEmpty() && stack.peek()[0] >= nums[i]){
                stack.pop();
            }
            nsr[i] = stack.isEmpty() ? nums.length:stack.peek()[1];
            stack.push(new int[]{nums[i], i});
        }
        return nsr; 
    }

    static int[] previousSmallerToLeft(int[] nums){
        Deque<int[]> stack = new ArrayDeque<>();
        int[] psl = new int[nums.length];
        for(int i=0; i<nums.length; i++){
            while(!stack.isEmpty() && stack.peek()[0] >= nums[i]){
                stack.pop();
            }
            psl[i] = stack.isEmpty() ? -1:stack.peek()[1];
            stack.push(new int[]{nums[i], i});
        }
        return psl; 
    }
}