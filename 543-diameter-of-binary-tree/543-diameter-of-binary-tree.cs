/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     public int val;
 *     public TreeNode left;
 *     public TreeNode right;
 *     public TreeNode(int val=0, TreeNode left=null, TreeNode right=null) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
public class Solution {
    private int maxDiameter;
    
    private int getLongestConnectedCnt(TreeNode root) {
        if(root == null) {
            return 0;
        }
        int leftCnt = getLongestConnectedCnt(root.left);
        int rightCnt = getLongestConnectedCnt(root.right);
        int connectedCnt = leftCnt + rightCnt + 1;
        this.maxDiameter = Math.Max(this.maxDiameter, connectedCnt - 1);
        return Math.Max(leftCnt, rightCnt) + 1;
    }
    
    
    public int DiameterOfBinaryTree(TreeNode root) {
        this.maxDiameter = 0;
        getLongestConnectedCnt(root);
        return this.maxDiameter;
    }
}