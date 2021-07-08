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

function dfs(node1, node2) {
    node1.val += node2.val;
    if(node1.left && node2.left) {
        dfs(node1.left, node2.left);
    }
    if(node1.right && node2.right) {
        dfs(node1.right, node2.right);
    }
    if(!node1.left && node2.left) {
        node1.left = node2.left;
    }
    if(!node1.right && node2.right) {
        node1.right = node2.right;
    }
}


var mergeTrees = function(root1, root2) {
    if(root1 === null) {
        return root2;
    }
    if(root2 === null) {
        return root1;
    }
    dfs(root1, root2);
    return root1;
};