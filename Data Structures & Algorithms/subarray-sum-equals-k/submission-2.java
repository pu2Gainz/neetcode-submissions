class Solution {
    public int subarraySum(int[] nums, int k) {
        HashMap<Integer, Integer> preMap = new HashMap<>();
        preMap.put(0, 1);
        int curSum = 0;
        int res = 0;
        for (int num : nums) {
            curSum += num;
            int targetSum = curSum - k;

            if (preMap.containsKey(targetSum)) {
                res += preMap.get(targetSum);
            }

            preMap.put(curSum, preMap.getOrDefault(curSum, 0) + 1);
        }

        return res;
    }
}