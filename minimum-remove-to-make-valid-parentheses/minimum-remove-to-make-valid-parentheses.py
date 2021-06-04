class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        st = []
        for i in range(len(s)):
            if s[i] != '(' and s[i] != ')': continue
                
            if len(st) > 0 and st[-1][0] == '(' and s[i] == ')':
                st.pop()
                continue
            st.append((s[i], i))
        
        removed_idx_set = set([idx for _, idx in st])
        
        ans = []
        for i in range(len(s)):
            if i in removed_idx_set: continue
            ans.append(s[i])
            
        return "".join(ans)
        