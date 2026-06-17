class Solution {

  

    public int f(int i,int[] dp,int[] nums) {
        if (i == 0) return nums[0];
        if (i == 1) return Math.max(nums[0], nums[1]);

        if (dp[i] != -1) return dp[i];

        dp[i] = Math.max(f(i - 1,dp,nums), f(i - 2,dp,nums)+ nums[i]);
        return dp[i];
    }

    public int rob(int[] nums) {
        int n = nums.length;

        if (n == 0) return 0;
        if (n == 1) return nums[0];
        int[] nums1 = Arrays.copyOfRange(nums, 0, n-1);
        int[] nums2 = Arrays.copyOfRange(nums, 1, n);
        int[] dp1 = new int[n-1];
        int[] dp2 = new int[n-1];
        Arrays.fill(dp1, -1);
        Arrays.fill(dp2, -1);

        return Math.max(f(n - 2,dp1,nums1) , f(n-2,dp2,nums2));
    }
}
