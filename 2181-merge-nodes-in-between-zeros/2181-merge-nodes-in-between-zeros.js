var mergeNodes = function(head) {
    const dummyNode = new ListNode();
    let mergedNode = dummyNode;
    let cur = head;
    
    while(cur) {
        if(cur.val === 0 && cur.next) {
            mergedNode.next = new ListNode();
            mergedNode = mergedNode.next;
        }
        mergedNode.val += cur.val;
        cur = cur.next;
    }
    
    return dummyNode.next;
};