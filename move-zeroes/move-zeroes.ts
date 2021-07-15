/**
 Do not return anything, modify nums in-place instead.
 */

function findNonZeroIdx(nums: number[], start:number): number {
    for(let i = start; i < nums.length; i++) {
        if(nums[i] !== 0) {
            return i;
        }
    }
    return -1;
}


function moveZeroes(nums: number[]): void {
    const isValidIdx = (idx) => idx >= 0 && idx < nums.length; 
    let slow = nums.indexOf(0, 0)
    let fast = findNonZeroIdx(nums, slow);
    while(isValidIdx(slow) && isValidIdx(fast)) {
        [nums[slow], nums[fast]] = [nums[fast], nums[slow]];
        slow = nums.indexOf(0, slow);
        fast = findNonZeroIdx(nums, fast);
    }
};