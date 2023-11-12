class Solution {
    public boolean reorderedPowerOf2(int n) {
        LinkedList<Integer> set = new LinkedList<>();
        int x =1;
        
        while (x < Math.pow(10,9)){
            set.add(x);
            x = x*2;
        }
        
        int a[] = count(n);
        
        for (int i = 0; Math.pow(2,i) < Math.pow(10,9); i++){
            if (Arrays.equals(a,count(set.get(i))))
                return true;
        }
        return false;
        
        // Store the counts of each number
        
    }
    
    public int[] count(int n){
        int[] counts = new int[10];
        
        while (n > 0){
            int rem = n%10;
            counts[rem]++;
            n /= 10;
        }
        return counts;
    }
}