function getMaxLen(cuts: number[]): bigint {
    let maxLen: number = 0;
    cuts.sort((a, b) => a-b)
        .reduce((prev, cur) => {
        maxLen = Math.max(maxLen, cur - prev)
        return cur
    });
    return BigInt(maxLen);
}

function maxArea(h: number, w: number, horizontalCuts: number[], verticalCuts: number[]): number {
    const maxH: bigint = getMaxLen([...horizontalCuts, 0, h]);
    const maxW: bigint = getMaxLen([...verticalCuts, 0, w]);
    return Number(maxH * maxW % 1000000007n);
};