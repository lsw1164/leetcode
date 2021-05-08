function minMoves(nums: number[]): number {
    const minVal = Math.min(...nums);
    return nums.reduce((prev, cur) => prev + cur - minVal, 0);
};