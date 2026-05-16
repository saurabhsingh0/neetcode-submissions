class Solution {
    public int[] dailyTemperatures(int[] temperatures) {
        Deque<Integer> stack = new ArrayDeque<>(); //only for indices
        int n = temperatures.length;
        int[] answers = new int[n];
        for(int i=0; i<n; i++){
            while(!stack.isEmpty() && temperatures[i] > temperatures[stack.peek()]){
                int idx = stack.pop();
                answers[idx] = i-idx; 
            }
            stack.push(i);
        }
        return answers;

    }
}
