class Solution {
    public int maxProfit(int[] prices) {
        int left = 0;
        int max = 0;
        
        for (int r = 0; r < prices.length; r++) {
            if (prices[r] < prices[left]) {
                left = r;
            } else {
                max = Math.max(max, prices[r] - prices[left]);
            }
        }

        return max;
    }
}
