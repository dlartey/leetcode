class Solution {
    public boolean isPowerOfThree(int n) {
        int low = 0;
        int high = n;
        
        while (low <= high){
            int mid = low + (high - low)/2;
            
            if (Math.pow(3,mid) == n)
                return true;
            
            if (Math.pow(3,mid) > n)
                high = mid-1;
            
            if (Math.pow(3,mid) < n)
                low = mid+1;
        }
        return false;
    }
}