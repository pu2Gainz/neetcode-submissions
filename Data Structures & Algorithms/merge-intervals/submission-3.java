class Solution {
    public int[][] merge(int[][] intervals) {
        Arrays.sort(intervals, (a, b) -> {
            if(a[0] == b[0]) return Integer.compare(a[1], b[1]);
            return Integer.compare(a[0], b[0]);
        });

        ArrayDeque<int[]> stack = new ArrayDeque<>();
        for (int[] interval: intervals) {
            if (!stack.isEmpty() && stack.peek()[1] >= interval[0]) {
                int[] prevInterval = stack.peek();
                stack.pop();
                int[] newInterval = {prevInterval[0], Math.max(prevInterval[1], interval[1])};
                stack.push(newInterval);
            } else {
                stack.push(interval);
            }
        }

        return stack.toArray(new int[0][]);
    }
}
