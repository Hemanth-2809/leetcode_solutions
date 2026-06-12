class Solution {
    public int findMin(int[] nums) {
        int left = 0;
        int right = nums.length -1;
        int mid;
        int minele = 999;
        while(left<=right){
            mid = (left+right+1)/2;
            if (nums[left]<nums[mid]){
                minele = Math.min(nums[left],minele);
                left = mid+1;
            }
            else{
                minele = Math.min(nums[mid],minele);
                right = mid-1;
            }
            
        }
        return minele;
    }
}
