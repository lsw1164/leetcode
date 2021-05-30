# """
# This is Master's API interface.
# You should not implement it, or speculate about its implementation
# """
# class Master:
#     def guess(self, word: str) -> int:

class Solution:
    def findSecretWord(self, wordlist: List[str], master: 'Master') -> None:
        N = len(wordlist)
        WORD_LEN = 6
        
        def guess(w1, w2):
            cnt = 0
            for i in range(WORD_LEN):
                if w1[i] == w2[i]: cnt += 1
            return cnt
            
        guess_mat = [[0 for _ in range(N)] for __ in range(N)] 
        match_cnts = [0]*N
        for i in range(N):
            for j in range(i, N):
                guess_cnt = guess(wordlist[i], wordlist[j])
                guess_mat[j][i] = guess_mat[i][j] = guess_cnt
                match_cnts[i] += guess_cnt
                match_cnts[j] += guess_cnt
                
        candidates = sorted(range(N), key=lambda c: match_cnts[c]) 
        
        while len(candidates) > 0:
            idx = candidates.pop()
            word = wordlist[idx]
            match_cnt = master.guess(word)
            if match_cnt == WORD_LEN: break
            candidates = list(filter(lambda c: guess_mat[idx][c] == match_cnt, candidates))
        