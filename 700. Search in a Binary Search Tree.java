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
    TreeNode node;
    public TreeNode searchBST(TreeNode root, int val) {
        helper(root,val);
        return node;
    }
    public void helper(TreeNode root,int val){
        if(root != null){
            helper(root.left,val);
            if(root.val==val){
                node = root;
            }
            helper(root.right,val);
        }
    }
}