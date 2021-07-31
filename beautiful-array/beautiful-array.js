/**
 * @param {number} n
 * @return {number[]}
 */
var beautifulArray = function(n) {
    let arr = [1];
    
    while(arr.length < n) {
        const odds = arr.map(num => 2*num - 1);
        const evens = arr.map(num => 2*num);
        arr = [...odds, ...evens]
    }
    
    return arr.filter(num => num <= n);
};