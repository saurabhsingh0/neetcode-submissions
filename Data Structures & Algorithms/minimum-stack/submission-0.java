class MinStack {

    private static Stack<Integer> stack;
    private static Stack<Integer> minStack;

    public MinStack() {
        this.stack = new Stack();
        this.minStack = new Stack();
    }
    
    public void push(int val) {
        this.stack.push(val);
        if(this.minStack.isEmpty() || val <= this.minStack.peek()){
            this.minStack.push(val);
        }
    }
    
    public void pop() {
        int val = this.stack.pop();
        if(this.minStack.peek() == val){
            this.minStack.pop();
        }
        
    }
    
    public int top() {
        return this.stack.peek();
    }
    
    public int getMin() {
        return this.minStack.peek();
    }
}
