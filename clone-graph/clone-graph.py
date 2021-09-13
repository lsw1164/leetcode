"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node: return None
        
        visit = [False] * 101
        cloned_node_table = [None] * 101
        
        def get_cloned_node(val):
            nonlocal cloned_node_table 
            if not cloned_node_table[val]:
                cloned_node_table[val] = Node(val)
            return cloned_node_table[val]
            
        def dfs(node):
            nonlocal cloned_node_table, visit
            if not node: return None
            visit[node.val] = True
            cloned_node = get_cloned_node(node.val)
            
            for neighbor in node.neighbors:
                cloned_node_neighbor = get_cloned_node(neighbor.val)
                cloned_node.neighbors.append(cloned_node_neighbor)
                if visit[neighbor.val]: continue
                dfs(neighbor)
            
        dfs(node)
        
        return get_cloned_node(node.val)
        
        