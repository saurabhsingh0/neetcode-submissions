class Solution {
    public int search(int[] nums, int target) {
        int pivot = getMinIndex(nums);
        if(nums[pivot] == target) return pivot;
        else if(target > nums[pivot] && target <= nums[nums.length-1]) {
            return binarySearch(nums, pivot, nums.length-1, target);
        }
        else return binarySearch(nums, 0, pivot-1, target);
    }

    public static int binarySearch(int[] arr, int low, int high, int target){
        if(low<=high){
            int mid = low + (high-low)/2;
            if(arr[mid] == target) return mid;
            else if(arr[mid] < target) return binarySearch(arr, mid+1, high, target);
            else return binarySearch(arr, low, mid-1, target);
        }
        return -1;
    }

    public int getMinIndex(int[] nums) {
        int low = 0, high = nums.length-1;
        int N = nums.length;
        while(low <=high) {
            int mid = low + (high-low)/2;
            if(nums[low] <= nums[high]) break; //sub-array is sorted
            if(nums[low] <= nums[mid]){
                low = mid + 1;
            }
            else high = mid;
        }
        return low;
    }
}
