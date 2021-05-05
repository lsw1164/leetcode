#define MAX(a,b) ((a) > (b) ? (a) : (b))
class Solution {
public:
    int jump(vector<int>& nums) {
        if(nums.size() <= 1) {
            return 0;
        }
        int minJumpCnt = 1;
        int curMaxPos = nums[0];
        int nextMaxPos = nums[0];
        for(int pos = 1; pos < nums.size()-1; pos++) {
            nextMaxPos = MAX(nextMaxPos, pos + nums[pos]);
            if(pos == curMaxPos) {
                minJumpCnt++;
                curMaxPos = nextMaxPos;
            }
        }
        return minJumpCnt;
        
    }
};