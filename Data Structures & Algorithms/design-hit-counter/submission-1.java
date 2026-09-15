class HitCounter {
    private Queue<Integer> hits;

    public HitCounter() {
        this.hits = new ArrayDeque<>();
    }
    
    public void hit(int timestamp) {
        this.hits.offer(timestamp);
    }
    
    public int getHits(int timestamp) {
        while (!hits.isEmpty()) {
            int diff = timestamp - this.hits.peek();
            if (diff >= 300) this.hits.poll();
            else break;
        }
        return this.hits.size();
    }
}

/**
 * Your HitCounter object will be instantiated and called as such:
 * HitCounter obj = new HitCounter();
 * obj.hit(timestamp);
 * int param_2 = obj.getHits(timestamp);
 */
