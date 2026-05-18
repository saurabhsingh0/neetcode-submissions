class KthLargest {

    private static PriorityQueue<Integer> minHeap;
    private static int K;
    public KthLargest(int k, int[] nums) {
        minHeap = new PriorityQueue<>();
        K = k;
        for(int num: nums){
            add(num);
        }
    }
    
    public int add(int val) {
        minHeap.offer(val);
        if(minHeap.size() > K){
            minHeap.poll();
        }
        return minHeap.peek();
    }
}
