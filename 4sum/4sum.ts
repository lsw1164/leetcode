function fourSum(nums: number[], target: number): number[][] {
    nums.sort((a,b) => a-b);
    const hashMap = new Map<string, number[]>();
    
    for(let i = 0; i < nums.length - 3; i++) {
        for(let j = i+1; j < nums.length - 2; j++) {
            for(let k = j+1; k < nums.length - 1; k++) {
                for(let l = k+1; l < nums.length; l++) {
                    if(nums[i] + nums[j] + nums[k] + nums[l] !== target) {
                        continue;
                    }
                    const key = `${nums[i]},${nums[j]},${nums[k]},${nums[l]}`;
                    if(hashMap.has(key)) {
                        continue;
                    }
                    hashMap.set(key, [nums[i], nums[j], nums[k], nums[l]]);
                }
            }
        }
    }
    return [...hashMap.values()];
};