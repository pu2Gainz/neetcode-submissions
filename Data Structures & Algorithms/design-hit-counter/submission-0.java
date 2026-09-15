class HitCounter {
    private HashMap<Integer, Integer> hitMap;

    public HitCounter() {
        this.hitMap = new HashMap<>();
    }
    
    public void hit(int timestamp) {
        this.hitMap.put(timestamp, hitMap.getOrDefault(timestamp, 0) + 1);
    }
    
    public int getHits(int timestamp) {
        int numOfHits = 0;
        for (Map.Entry<Integer, Integer> item : this.hitMap.entrySet()) {
            if (item.getKey() > timestamp - 300) {
                numOfHits += item.getValue();
            }
        }
        return numOfHits;
    }
}

/**
 * Your HitCounter object will be instantiated and called as such:
 * HitCounter obj = new HitCounter();
 * obj.hit(timestamp);
 * int param_2 = obj.getHits(timestamp);
 */
