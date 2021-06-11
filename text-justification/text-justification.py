class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        
        def get_last_idx(start_idx):
            sum_of_len = 0
            idx = start_idx
            st = []
            while idx < len(words):
                word = words[idx]
                sum_of_len += len(word)
                st.append(word)
                if sum_of_len + len(st) - 1 > maxWidth:
                    break
                idx += 1
            return idx - 1
                
            
        def pack(left, right):
            count = right-left+1
            if count == 1:
                return words[left].ljust(maxWidth)
            
            if len(words)-1 == right:
                return " ".join(words[left:right+1]).ljust(maxWidth)
                
            sum_of_len = 0
            for i in range(left, right+1):
                sum_of_len += len(words[i])
                
            spaces = maxWidth - sum_of_len
            each_space = spaces // (count-1)
            left_spaces = spaces % (count-1)
            
            pacK_list = []
            for i in range(left, right):
                pad = each_space
                if left_spaces > 0: 
                    pad += 1
                    left_spaces -= 1
                width = len(words[i]) + pad
                pacK_list.append(words[i].ljust(width))
            pacK_list.append(words[right])
            return "".join(pacK_list)
            
            
        left, right = 0, 0
        output = []
        
        while left < len(words):
            right = get_last_idx(left)
            output.append(pack(left, right))
            left = right+1
        return output
                