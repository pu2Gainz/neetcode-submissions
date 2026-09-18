class Solution {
    public boolean checkInclusion(String s1, String s2) {
        if (s1.length() > s2.length()) return false;

        int[] m1 = new int[26];
        int[] m2 = new int[26];
    
        for (char c : s1.toCharArray()) {
            m1[c - 'a']++;
        }

        for (int i = 0; i < s1.length(); i++) {
            m2[s2.charAt(i) - 'a']++;
        }

        if (Arrays.equals(m1, m2)) return true;

        for (int right = s1.length(); right < s2.length(); right++) {
            m2[s2.charAt(right) - 'a']++;
            m2[s2.charAt(right - s1.length()) - 'a']--;
            if (Arrays.equals(m1, m2)) return true;
        }

        return false;
    }
}