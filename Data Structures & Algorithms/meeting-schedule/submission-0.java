/**
 * Definition of Interval:
 * public class Interval {
 *     public int start, end;
 *     public Interval(int start, int end) {
 *         this.start = start;
 *         this.end = end;
 *     }
 * }
 */

class Solution {
    public boolean canAttendMeetings(List<Interval> intervals) {
        if(intervals == null || intervals.size() == 0) {
            return true;
        }
        intervals.sort((a, b) -> Integer.compare(a.start, b.start));
        for(int i=1; i<intervals.size(); i++){
            Interval interval = intervals.get(i);
            Interval prevInterval = intervals.get(i-1);
            if (prevInterval.end > interval.start) {
                return false;
            }
        }
        return true;
    }
}
