class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        
        // Loop through each string in the string array and convert it to a char array and sort
        // then store this char array and the (words) in a hashmap
        
        //e.g. HashMap<Character[],List<String> m = new HashMap<>()
        // m -> [a,e,t] - (eat, tea), 
        
        // then afterwards loop through the hashmap and add all the anagrams to the final list
        // to be returned
        
        List<List<String>> ret = new ArrayList<>();
        HashMap<String, List<String>> map = new HashMap<>();
        for (String s: strs){
            char[] t = s.toCharArray();
            Arrays.sort(t);
            String new1 = new String(t);
            
            
            if (!map.containsKey(new1)){
                List<String> temp = new ArrayList<>();
                temp.add(s);
                map.put(new1,temp);
            }else{
                map.get(new1).add(s);
            }
        }
        
        
        return new ArrayList(map.values());
        
    }
}