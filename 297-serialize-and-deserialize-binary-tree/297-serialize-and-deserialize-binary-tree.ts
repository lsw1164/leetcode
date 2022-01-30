/**
 * Definition for a binary tree node.
 * class TreeNode {
 *     val: number
 *     left: TreeNode | null
 *     right: TreeNode | null
 *     constructor(val?: number, left?: TreeNode | null, right?: TreeNode | null) {
 *         this.val = (val===undefined ? 0 : val)
 *         this.left = (left===undefined ? null : left)
 *         this.right = (right===undefined ? null : right)
 *     }
 * }
 */

/*
 * Encodes a tree to a single string.
 */

interface ISerializedNode {
    val: number;
    id: number;
    lId: number;
    rId: number;
}


let id: number = 1;
const getNewId = () => id++;
const resetId = () => id = 1;

function serialize(root: TreeNode | null): string {
    if(root === null) {
        return "";
    }
    
    
    const serializedNodeList: ISerializedNode[] = [];
    resetId();
    dfs(serializedNodeList, root, getNewId());
    
    return JSON.stringify(serializedNodeList);
};


function dfs(serializedNodeList: ISerializedNode[], node: TreeNode, id: number) {
    const lId = getNewId();
    const rId = getNewId();
    serializedNodeList.push({val: node.val, id, lId, rId});   
   
    if(node.left) {
        dfs(serializedNodeList, node.left, lId);
    }
    if(node.right) {
        dfs(serializedNodeList, node.right, rId);
    }
}

/*
 * Decodes your encoded data to tree.
 */
function deserialize(data: string): TreeNode | null {
    if(data.length === 0) {
        return null;
    }
    const serializedNodeList: ISerializedNode[] = JSON.parse(data)
    
    const hashMap = new Map<number, TreeNode>();
    
    serializedNodeList.forEach(serializedNode => {
        hashMap.set(serializedNode.id, new TreeNode(serializedNode.val));
    });
    
    serializedNodeList.forEach(serializedNode => {
        const node = hashMap.get(serializedNode.id);
        const lNode = hashMap.has(serializedNode.lId) ? hashMap.get(serializedNode.lId) : null;
        const rNode = hashMap.has(serializedNode.rId) ? hashMap.get(serializedNode.rId) : null;
        node.left = lNode;
        node.right = rNode;
    });
    
    return hashMap.has(1) ? hashMap.get(1) : null;
};


/**
 * Your functions will be called as such:
 * deserialize(serialize(root));
 */