var flatten = function(head) {
    let prevNode = null;
    let curNode = null;
    
    function dfs(node) {
        while(node) {
            prevNode = curNode;
            curNode = node;
            const nextNode = curNode.next;
            
            if(prevNode) {
                prevNode.next = curNode;
                prevNode.child = null;
            }
            curNode.prev = prevNode;
            
            if(node.child) {
                dfs(node.child);
            }
            node = nextNode;
        }
    }
    
    dfs(head);
    
    return head;
};


