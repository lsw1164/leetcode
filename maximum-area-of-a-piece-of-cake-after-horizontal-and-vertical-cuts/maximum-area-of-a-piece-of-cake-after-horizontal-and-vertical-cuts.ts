const MOD = 1000000007n;

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
    return Number(getMaxLen([...horizontalCuts, 0, h]) * getMaxLen([...verticalCuts, 0, w]) % MOD);
};