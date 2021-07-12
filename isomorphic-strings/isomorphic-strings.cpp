class Solution {
public:
    bool isIsomorphic(string s, string t) {
        vector<int> replace_map(128);
        vector<bool> visit(128);
        fill(replace_map.begin(), replace_map.end(), -1);
        fill(visit.begin(), visit.end(), false);
        
        for(int i = 0; i < s.size(); i++) {
            const int src = s[i], target = t[i];
            if(replace_map[src] == -1) {
                replace_map[src] = target;
                if(visit[target]) {
                    return false;
                }
                visit[target] = true;
                continue;
            }
            if(replace_map[src] != target) {
                return false;
            }
        }
        return true;
    }
};