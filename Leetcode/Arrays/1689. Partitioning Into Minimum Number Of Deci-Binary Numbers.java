class Solution {
    public int minPartitions(String n) {
        int maxi = Integer.MIN_VALUE;
        for (int j = 0; j < n.length(); j++){
            maxi = Math.max(maxi,Integer.parseInt(String.valueOf(n.charAt(j))));
        }
        return maxi;
    }
}