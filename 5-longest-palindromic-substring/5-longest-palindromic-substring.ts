function longestPalindrome(s: string): string {
    const memo = Array.from({ length : s.length })
                      .map(() => Array(s.length).fill(null));
    
    for(let len = s.length; len > 0; len--) {
        for(let left = 0; left + len - 1 < s.length; left++) {
            const right = left + len - 1;
            if(isPalindrome(s, left, right)) {
                return s.substring(left, right+1);
            }
        }
    }
    
    function isPalindrome(str, left, right) {
        if(left < 0 || left >= str.length || right < 0 || right >= str.length) {
            return false;
        }
        if(memo[left][right] !== null) {
            return memo[left][right];
        }
        
        const len = right - left + 1;
        if(len <= 2) {
            memo[left][right] = str[left] === str[right];
        } else {
            memo[left][right] = str[left] === str[right] && isPalindrome(str, left + 1, right - 1);
        }
        
        return memo[left][right];
    } 

};
