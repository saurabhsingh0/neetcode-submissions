/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */

class Solution {
    public List<List<Integer>> levelOrder(TreeNode root) {
        List<List<Integer>> result = new ArrayList<>();
        Queue<TreeNode> queue = new LinkedList<>();
        queue.offer(root);
        while(!queue.isEmpty()){
            int len = queue.size();
            System.out.println(len);
            List<Integer> temp = new ArrayList<>();
            for(int i=0; i<len; i++){
                TreeNode node = queue.poll();
                
                if(node != null){
                    temp.add(node.val);
                    queue.offer(node.left);
                    queue.offer(node.right); 
                }
            }
            if(!temp.isEmpty()){
                result.add(temp);
            }
        }
        return result;
    }
}
