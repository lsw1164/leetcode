/**
 * @param {number[][]} grid
 * @return {number}
 */

var islandPerimeter = function(grid) {
    let ans = 0
    const ROW = grid.length, COL = grid[0].length;
    
    const diffR = [0, 0, 1, -1];
    const diffC = [-1, 1, 0, 0];
    
    for(let r = 0; r < ROW; r++) {
        for(let c = 0; c < COL; c++) {
            if(grid[r][c] !== 1) {
                continue;
            }
            for(let i = 0; i < 4; i++) {
                const nextR = r + diffR[i];
                const nextC = c + diffC[i];
                if(nextR < 0 || nextR >= ROW || nextC < 0 || nextC >= COL) {
                    ans++;
                    continue;
                } 
                if(grid[nextR][nextC] === 0) {
                    ans++;
                }
            }
            
        }
    }
    return ans;
};