class Solution:
    def removeDuplicates(self, s: str) -> str:
        st = []
        for ch in s:
            if len(st) > 0 and ch == st[-1]:
                st.pop()
                continue
            st.append(ch)
            
        return "".join(st)