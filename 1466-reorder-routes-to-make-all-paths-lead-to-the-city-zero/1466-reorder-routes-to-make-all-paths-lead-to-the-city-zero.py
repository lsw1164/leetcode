from collections import deque
class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        graph = [[] for _ in range(n)]
        visit = [False for _ in range(n)]
        
        for u, v in connections:
            graph[u].append([v, True])
            graph[v].append([u, False])
        
        que = deque()
        que.append(0)
        visit[0] = True
        
        reorder_cnt = 0
        while len(que) > 0:
            dest = que.popleft()
            
            for src, should_reorder in graph[dest]:
                if visit[src]: continue
                    
                visit[src] = True
                que.append(src)
                
                if should_reorder: 
                    reorder_cnt += 1

        return reorder_cnt