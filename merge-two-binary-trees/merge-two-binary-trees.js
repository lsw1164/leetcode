/**
 * Definition for a binary tree node.
 * function TreeNode(val, left, right) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.left = (left===undefined ? null : left)
 *     this.right = (right===undefined ? null : right)
 * }
 */
/**
 * @param {TreeNode} root1
 * @param {TreeNode} root2
 * @return {TreeNode}
 */

function dfs(node1, node2, mergedNode) {
    mergedNode.val = (node1?.val ?? 0) + (node2?.val ?? 0);
    
    if(node1?.left || node2?.left) {
        mergedNode.left = new TreeNode(); 
        dfs(node1?.left, node2?.left, mergedNode.left);
    }
    
    if(node1?.right || node2?.right) {
        mergedNode.right = new TreeNode(); 
        dfs(node1?.right, node2?.right, mergedNode.right);
    }
}


var mergeTrees = function(root1, root2) {
    if(root1 === null) {
        return root2;
    }
    if(root2 === null) {
        return root1;
    }
    const mergedRoot = new TreeNode();
    dfs(root1, root2, mergedRoot);
    return mergedRoot;
};