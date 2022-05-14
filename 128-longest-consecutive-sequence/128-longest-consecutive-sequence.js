/**
 * @param {number[]} nums
 * @return {number}
 */
var longestConsecutive = function(nums) {
    if(nums.length <= 1) {
        return nums.length;
    }
    
    const set = new Set(nums);
    
    let longestLen = 0;
    
    nums.forEach(num => {
        
        if(!set.has(num) || set.has(num - 1)) {
            return;
        }
        
        let curLen = 1;
        set.delete(num);
        
        while(set.has(num + 1)) {
            set.delete(num + 1);
            num++;
            curLen++;
        }
        
        longestLen = Math.max(longestLen, curLen);
    });
    
    return longestLen;
};