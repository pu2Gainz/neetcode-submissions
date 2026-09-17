class Solution {
    public int characterReplacement(String s, int k) {
        char[] arr = s.toCharArray();
        HashMap<Character, Integer> count = new HashMap<>();
        int left = 0;
        int maxLength = 0;
        int maxFreq = 0;
        for (int right = 0; right < s.length(); right++) {
            count.put(arr[right], count.getOrDefault(arr[right], 0) + 1);
            maxFreq = Math.max(maxFreq, count.get(arr[right]));
            int length = right - left + 1;
            while (length - maxFreq > k) {
                count.put(arr[left], count.get(arr[left]) - 1);
                left++;
                length--;
            }

            maxLength = Math.max(maxLength, length);
        }

        return maxLength;
    }
}
