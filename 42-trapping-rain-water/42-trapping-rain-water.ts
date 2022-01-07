function trap(height: number[]): number {
    const leftCumulaitveList = Array(height.length).fill(0);
    const rightCumulaitveList = Array(height.length).fill(0);
    let lMax = 0;
    let rMax = 0;
    
    height.forEach((h, lIdx) => {
        const rIdx = height.length - 1 - lIdx;
        lMax = Math.max(lMax, h);
        rMax = Math.max(rMax, height[rIdx]);
        leftCumulaitveList[lIdx] = lMax;
        rightCumulaitveList[rIdx] = rMax;
    });
    
    return height.reduce((acc, cur, idx) => {
        const minH = Math.min(leftCumulaitveList[idx], rightCumulaitveList[idx]);
        return acc + Math.max(minH - cur, 0);
    }, 0);
    
}