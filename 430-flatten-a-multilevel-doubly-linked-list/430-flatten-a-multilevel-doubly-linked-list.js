var flatten = function(head) {
    flattenRecursive(head);
    return head;
};

function flattenRecursive(node) {
    let cur = node;
    
    while(cur) {
        const nextNode = cur.next;
        const childNode = cur.child;

        if(childNode) {
            cur.next = childNode;
            childNode.prev = cur;
            const lastChild = flattenRecursive(childNode);
            lastChild.next = nextNode;
            if(nextNode) {
                nextNode.prev = lastChild;
            }
            cur.child = null
        }
        cur = nextNode;
    }
    
    let lastNode = node;
    while(node) {
        lastNode = node;
        node = node.next;
    }
    return lastNode;
}
