class Solution {
    public List<String> fullJustify(String[] words, int maxWidth) {
        List<String> res = new ArrayList<>();
        List<String> line = new ArrayList<>();
        int length = 0, i = 0;

        while (i < words.length) {
            if (length + words[i].length() + line.size() <= maxWidth) {
                line.add(words[i]);
                length += words[i].length();
                i++;
            } else {
                int extraSpace = maxWidth - length;
                int remainder = extraSpace % Math.max(1, (line.size() - 1));
                int space = extraSpace / Math.max(1, (line.size() - 1));
                for (int j = 0; j < Math.max(1, line.size() - 1); j++) {
                    line.set(j, line.get(j) + " ".repeat(space));
                    if (remainder > 0) {
                        line.set(j, line.get(j) + " ");
                        remainder--;
                    }
                }

                res.add(String.join("", line));
                line.clear();
                length = 0;
            }
        }

        String lastLine = String.join(" ", line);
        int trailSpace = maxWidth - lastLine.length();
        res.add(lastLine + " ".repeat(trailSpace));

        return res;
    }
}