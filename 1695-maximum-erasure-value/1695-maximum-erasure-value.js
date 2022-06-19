/**
 * @param {number[]} nums
 * @return {number}
 */
var maximumUniqueSubarray = function(nums) {
    let sum = 0;
    const cumulativeSum = nums.map(num => {
        sum += num;
        return sum;
    });
    
    const getRangeCumulativeSum = (l, r) => {
        return l > 0 ? cumulativeSum[r] - cumulativeSum[l - 1] : cumulativeSum[r];
    }

    
    const hashMap = new Map();
    
    let maxSum = 0;
    let left = 0;
    let right = 0;
    while(right < nums.length) {
        
        if(hashMap.has(nums[right])) {
            left = Math.max(left, hashMap.get(nums[right]) + 1);
        } 
        
        hashMap.set(nums[right], right);
        maxSum = Math.max(maxSum, getRangeCumulativeSum(left, right));
        right++;
    }
    
    return maxSum;
    
};