class Solution {
    public List<List<String>> findDuplicate(String[] paths) {
        List<List<String>> ret = new ArrayList<>();
        
        HashMap<String,List<String>> map = new HashMap<>();
        // IDEA:
        // loop through the paths array, then
        // 1: split using " ", and store the 1st index as the root
        // 2: store the word in () in a hashmap with the full path
        // add each nth occurence to the hashmap
        // then once we done this, we loop over the map and add all
        // keys with list.size() > 2 into the ret list, and return it
        
        
        // to get the content, we only need to look for (
        // this is because we can get the filename using substring(0,pos_of_( )
        // and we can get the content name using substring(pos_of_(+1, len )
        for (int i = 0; i < paths.length; i++){
            String[] temp = paths[i].split(" ");
            String root = temp[0];
            
            for (int j = 1; j < temp.length; j++){
                int index = temp[j].indexOf("(");
                String fileName = root+"/"+temp[j].substring(0,index);
                String fileContent = temp[j].substring(index+1,temp[j].length());
                
                if (!map.containsKey(fileContent)){
                    map.put(fileContent,new ArrayList<>());
                    map.get(fileContent).add(fileName);
                }else{
                     map.get(fileContent).add(fileName);
                }
            }
            
        }
        
        for (String k : map.keySet()){
            if (map.get(k).size() > 1){
                ret.add(map.get(k));
            }
        }
        
        return ret;
    }
}