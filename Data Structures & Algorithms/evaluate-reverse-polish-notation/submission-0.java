class Solution {
    public int evalRPN(String[] tokens) {
        Stack<Integer> stack = new Stack<>();
        for(String token: tokens){
                if(token.equals("+")){
                    int a = stack.pop();
                    int b = stack.pop();
                    stack.push(b+a);        
                }
                else if(token.equals(new String("-"))){
                    int a = stack.pop();
                    int b = stack.pop();
                    stack.push(b-a);
                }    
                else if (token.equals(new String("*"))) {
                    int a = stack.pop();
                    int b = stack.pop();
                    stack.push(b*a);
                }    
                else if(token.equals(new String("/"))){
                    int a = stack.pop();
                    int b = stack.pop();
                    stack.push(b/a);
                }    
                else {
                    int val = Integer.parseInt(token);
                    stack.push(val);
                }
        }
        int ans = stack.pop();
        return ans;
    }
}
