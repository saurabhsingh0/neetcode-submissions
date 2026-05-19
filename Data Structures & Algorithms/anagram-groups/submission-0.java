class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        Map<String,List<String>> map = new HashMap<>();
        for(String s: strs){
            char[] temp = s.toCharArray();
            Arrays.sort(temp);
            String t = new String(temp);
            map.computeIfAbsent(t, k-> new ArrayList<>()).add(s);
        }
        return new ArrayList<>(map.values());
    }
}
