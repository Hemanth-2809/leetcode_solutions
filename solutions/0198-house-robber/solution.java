class Solution {

    int[] dp;
    int[] nums;

    public int f(int i) {
        if (i == 0) return nums[0];
        if (i == 1) return Math.max(nums[0], nums[1]);

        if (dp[i] != -1) return dp[i];

        dp[i] = Math.max(f(i - 1), f(i - 2) + nums[i]);
        return dp[i];
    }

    public int rob(int[] nums) {
        int n = nums.length;

        if (n == 0) return 0;
        if (n == 1) return nums[0];

        this.nums = nums;
        this.dp = new int[n];
        Arrays.fill(dp, -1);

        return f(n - 1);
    }
}
