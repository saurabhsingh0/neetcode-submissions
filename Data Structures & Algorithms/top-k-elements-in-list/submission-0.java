class Solution {
    public int[] topKFrequent(int[] nums, int k) {
        PriorityQueue<int[]> maxHeap = new PriorityQueue<>(
            (a,b) -> a[0] - b[0]
        );
        Map<Integer,Integer> freqMap = new HashMap<>();
        for(int num: nums){
            freqMap.put(num, freqMap.getOrDefault(num, 0)+1);
        }
        for(Map.Entry<Integer, Integer> entry: freqMap.entrySet()){
            maxHeap.offer(new int[]{entry.getValue(), entry.getKey()});
            if(maxHeap.size()>k) maxHeap.poll();
        }
        int[] ans = new int[k];
        int i=0;
        while(!maxHeap.isEmpty()){
            ans[i] = maxHeap.poll()[1];
            i++;
        }
        return ans;
    }
}