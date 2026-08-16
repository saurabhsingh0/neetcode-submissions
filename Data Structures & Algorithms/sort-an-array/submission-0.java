class Solution {
    public int[] sortArray(int[] nums) {
        mergeSort(nums, 0, nums.length-1);
        return nums;
    }

    private void mergeSort(int[] arr, int left, int right){
        if(left >= right) {
            return;
        }
        int mid = left +(right - left)/2;
        mergeSort(arr, left, mid);
        mergeSort(arr, mid+1, right);
        merge(arr, left, mid, right);
    }

    private void merge(int[] arr, int left, int mid, int right) {
        ArrayList<Integer> temp = new ArrayList<>();
        int i = left, j = mid+1;
        while(i<=mid && j<=right) {
            if(arr[i] <= arr[j]){
                temp.add(arr[i]);
                i++;
            }
            else {
                temp.add(arr[j]);
                j++;
            }
        }
        while(i<=mid){
            temp.add(arr[i]);
            i++;
        }

        while(j<=right){
            temp.add(arr[j]);
            j++;
        }

        for(i=left; i<=right; i++){
            arr[i] = temp.get(i-left);
        }
    }
}