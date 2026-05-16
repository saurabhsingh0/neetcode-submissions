class Solution {
    public boolean isValid(String s) {
        Stack<Character> stack = new Stack<>();
        Map<Character, Character> openToClose = new HashMap<>();
        openToClose.put('(', ')');
        openToClose.put('[',']');
        openToClose.put('{','}');
        for(int i=0; i<s.length(); i++){
            if(openToClose.containsKey(s.charAt(i))){
                stack.push(s.charAt(i));
                continue;
            }
            if(stack.size() > 0 && s.charAt(i) == openToClose.get(stack.peek())) {
                stack.pop();
            }
            else {
                return false;
            }
        }
        if(stack.size() > 0) return false;
        return true;
    }
}
