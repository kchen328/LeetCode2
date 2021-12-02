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
    public TreeNode mergeTrees(TreeNode root1, TreeNode root2) {
        //TreeNode n_node = new TreeNode();
        
        return helper(root1,root2);
        //return n_node;
    }
    public TreeNode helper(TreeNode r1, TreeNode r2) {
        TreeNode root = new TreeNode();
        
        if (r1 != null && r2 != null) {
            root.val = r1.val + r2.val;
            root.left = helper(r1.left,r2.left);
            root.right = helper(r1.right,r2.right);
        } else if (r1 == null && r2 != null){
            root.val = r2.val;
            root.left = helper(null,r2.left);
            root.right = helper(null,r2.right);
        } else if (r1 != null && r2 == null) {
            root.val = r1.val;
            root.left = helper(r1.left,null);
            root.right = helper(r1.right,null);
        } else {
            return null;
        }
        
        
        return root;
    }
}
