function permute(nums) {
    
    const permutes = [];
    
    function updatePermutes(pivot) {
        if(pivot === nums.length) {
           permutes.push([...nums]);
           return;
        }
        
        for(let i = pivot; i < nums.length; i++) {
            [nums[pivot], nums[i]] = [nums[i], nums[pivot]];
            updatePermutes(pivot+1);
            [nums[pivot], nums[i]] = [nums[i], nums[pivot]];
        }
    }
    
    updatePermutes(0);
    return permutes;
};