function jump(nums: number[]): number {
    let nextMaxPos = 0;
    let curMaxPos = 0;
    let minJumpCnt = 0;
    nums.forEach( (num, pos) => {
        nextMaxPos = Math.max(nextMaxPos, num + pos);
        if(curMaxPos === pos && pos < nums.length - 1) {
            curMaxPos = nextMaxPos;
            minJumpCnt++;
        }
    })
    return minJumpCnt;
};