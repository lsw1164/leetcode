from collections import deque  

class Solution:
    def minKnightMoves(self, x: int, y: int) -> int:
        dr = (2, 2, -2, -2, 1, 1, -1, -1)
        dc = (-1, 1, 1, -1, 2, -2, 2, -2)
        que = deque()
        visit = [[None for _ in range(601)] for __ in range(601)]
        
        sr, sc = 300, 300
        x += sr
        y += sc
        que.append((sr, sc ,0))
        visit[sr][sc] = True
        
        while len(que) > 0:
            r, c, cnt = que.popleft()
            if r == x and c == y: return cnt
            for i in range(len(dr)):
                nr = r + dr[i]
                nc = c + dc[i]
                if nr < 0 or nr >= 601 or nc < 0 or nc >= 601: continue
                if visit[nr][nc]: continue
                visit[nr][nc] = True
                que.append((nr, nc, cnt+1))
                
        return -1
    