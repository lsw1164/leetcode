class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        chain_len_by_word = {}
        for word in words:
            chain_len_by_word[word] = 1 if len(word) == 1 else None
            
        
        def get_chain_len(word):
            if not word in chain_len_by_word:
                return 0
            
            if chain_len_by_word[word] != None:
                return chain_len_by_word[word]
            
            max_len = 0
            for i in range(len(word)):
                cur_len = get_chain_len(word[:i] + word[i+1:])
                max_len = max(max_len, cur_len)
            chain_len_by_word[word] = max_len + 1
            return chain_len_by_word[word]
                
        
        max_len = 0
        for word in words:
            cur_len = get_chain_len(word)
            max_len = max(max_len, cur_len)
        return max_len
        