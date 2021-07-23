function threeSum(nums: number[]): number[][] {
    if(nums.length < 3) {
        return [];
    }
    
    nums.sort((a, b) => a - b);
    
    const hashMap = new Map();
    nums.forEach(num => {
        const value = hashMap.get(num) ?? 0;
        hashMap.set(num, value + 1);
    });
    
    const s = new Set<string>();
    
    for(let i = 0; i < nums.length - 1; i++) {
        for(let j = i + 1; j < nums.length; j++) {
            const third = -(nums[i] + nums[j]);
            if(!hashMap.has(third)) {
                continue;
            }
            if(third === nums[i] || third === nums[j]) {
                if(hashMap.get(third) < 2) continue;
                if(third === 0 && hashMap.get(third) < 3) continue;
            }
            s.add([nums[i], nums[j], third]
                  .sort((a,b) => a-b)
                  .join("#"));
        }
    }
    
    return [...s].map(triplets => triplets.split("#").map(num => +num))
};