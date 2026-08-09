class Solution {
    public int[][] kClosest(int[][] points, int k) {
        PriorityQueue<int[]> maxHeap = new PriorityQueue<>((a, b) -> {
            float distA = calcDist(a);
            float distB = calcDist(b);
            return Float.compare(distB, distA);
        });

        for(int[] point: points) {
            if(maxHeap.size() < k){
                maxHeap.offer(point);
            }    
            else {
                float top = calcDist(maxHeap.peek());
                float currentDist = calcDist(point);
                if (currentDist < top){
                    maxHeap.poll();
                    maxHeap.offer(point);
                }
            }
        }
        int[][] result = new int[maxHeap.size()][2];
        int i=0;
        while(!maxHeap.isEmpty()) {
            result[i] = maxHeap.poll();
            i++;
        }
        return result;
    }

    public static float calcDist(int[] points) {
        return (float)Math.sqrt(points[0]*points[0] + points[1]*points[1]);
    }

}
