class Solution:
    def isValid(self, s: str) -> bool:
        opens = ['(', '[', '{']
        close_to_open = {
            ')' : '(',
            ']' : '[',
            '}' : '{'
        }
        st = []
        for ch in s:
            if len(st) == 0 or ch in opens:
                st.append(ch)
                continue
            if st[-1] != close_to_open[ch]:
                return False
            st.pop()
            
        return len(st) == 0
                