class Solution {
    public boolean isStrictlyPalindromic(int n) {
        for (int i = 2; i <= n-2; i++){
            String s = Integer.toString(n,i);
            if (!checkPalindrome(s))
                return false;
        }
        return true;
        
    }
    
    public boolean checkPalindrome(String s){
        int n = s.length();
        for (int i = 0; i < n/2; i++){
            if (s.charAt(i) != s.charAt(n-i-1))
                return false;
        }
        return true;
    }
}