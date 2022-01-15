function maxPoints(points: number[][]): number {
    
    if(points.length === 1) {
        return Math.max(...points[0]);
    }
    
    const R = points.length;
    const C = points[0].length;
    
    const memo = Array(C).fill(0)
    let prevMax: number[] = points[0];
    
    for(let r = 1; r < R; r++) {
        for(let c1 = 0; c1 < C; c1++) {
            for(let c2 = 0; c2 < C; c2++) {
                const cost = Math.abs(c1 - c2);
                memo[c1] = Math.max(memo[c1], prevMax[c2] + points[r][c1] - cost);
            }
        }
        prevMax = [...memo];
    }
    
    return Math.max(...memo);
};