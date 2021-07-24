function firstMissingPositive(nums: number[]): number {
    if(!nums.includes(1)) {
        return 1;
    }
    
    nums.forEach((num, i) => {
        if(num <= 0 || num > nums.length) {
            nums[i] = 1;
        }
    });
    
    nums.forEach(num => {
        const idx = Math.abs(num) - 1
        nums[idx] = -Math.abs(nums[idx]);
    })
        
    for(const [idx, num] of nums.entries()) {
        if(num > 0) {
            return idx+1;
        }
    }
    return nums.length+1
};