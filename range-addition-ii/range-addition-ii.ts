function maxCount(m: number, n: number, ops: number[][]): number {
    if(ops.length === 0) {
        return m*n;
    }
    
    return ops.reduce(
        (acc: number[], cur: number[]) => [Math.min(acc[0], cur[0]), Math.min(acc[1], cur[1])]
        , [Infinity, Infinity]
    ).reduce((acc: number, cur: number) => acc * cur);
    
};