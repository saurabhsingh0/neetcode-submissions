class Solution {
    public int minEatingSpeed(int[] piles, int h) {
        int low = 1;
        int high = piles[0];
        for(int pile: piles){
            high = Math.max(high, pile);
        }
        int ans = high;
        while(low <= high){
            int rate = low + (high-low)/2;
            if(isValidRate(piles, rate, h)){
                ans = rate;
                high = rate - 1;
            }
            else {
                low = rate + 1;
            }
        }
        return ans;
    }

    private boolean isValidRate(int[] piles, int rate, int h) {
        int totalTime = 0;
        for(int pile: piles){
            totalTime += + Math.ceil((double)pile/rate);
        }

        return totalTime <= h ? true : false;
    }
}
