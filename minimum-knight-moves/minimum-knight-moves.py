from collections import deque  

class Solution:
    def minKnightMoves(self, x: int, y: int) -> int:
        if x == 0 and y == 0: return 0
        dr = (2, 2, -2, -2, 1, 1, -1, -1)
        dc = (-1, 1, 1, -1, 2, -2, 2, -2)
        que = deque()
        SIZE = 601
        mat = [[None for _ in range(SIZE)] for __ in range(SIZE)]
        sr, sc = SIZE//2, SIZE//2 
        x += sr
        y += sc
        from_start = (sr, sc, 0, True)
        from_target = (x, y, 0, False)
        que.append(from_start)
        que.append(from_target)
        mat[sr][sc] = from_start
        mat[x][y] = from_target
        
        while len(que) > 0:
            node = que.popleft()
            r, c, cnt, is_from_start = node
            for i in range(len(dr)):
                nr = r + dr[i]
                nc = c + dc[i]
                if nr < 0 or nr >= SIZE or nc < 0 or nc >= SIZE: continue
                next_node = (nr, nc, cnt + 1, is_from_start)
                if not mat[nr][nc]:
                    mat[nr][nc] = next_node
                    que.append(next_node)
                    continue
                elif mat[nr][nc][3] != is_from_start:
                    return mat[nr][nc][2] + cnt + 1
                
        return -1
    