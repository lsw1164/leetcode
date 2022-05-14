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
        
        if(!set.has(num)) {
            return;
        }
        
        let curLen = 1;
        set.delete(num);
        
        let leftSide = num - 1;
        let rightSide = num + 1;
        
        while(set.has(leftSide)) {
            set.delete(leftSide);
            curLen++;
            leftSide--;
        }
        
        while(set.has(rightSide)) {
            set.delete(rightSide);
            curLen++;
            rightSide++;
        }
        
        longestLen = Math.max(longestLen, curLen);
    });
    
    return longestLen;
};