class Solution:
    
    def judgePoint24(self, cards: List[int]) -> bool:
        
        operators = ['+', '-', '*', '/']
        
        def calc(n1, n2, op):
            if op == '+': return n1+n2
            if op == '-': return n1-n2
            if op == '*': return n1*n2
            if n2 == 0: return float('inf')
            return n1/n2
        

        def cacl_postfix_notation(postfix_notation):
            st = []
            for elem in postfix_notation:
                if elem in operators:
                    n2, n1 = st.pop(), st.pop()
                    ret = calc(n1, n2, elem)
                    st.append(ret)
                    continue
                st.append(elem)
            return st[-1]
        
        
        for ops in itertools.product(operators, repeat=3):
            for nums in itertools.permutations(cards):
                r1 = cacl_postfix_notation(nums + ops)
                r2 = cacl_postfix_notation(nums[:2] + (ops[0],) + nums[2:] + ops[1:])
                if abs(24 - r1) < 0.01: return True
                if abs(24 - r2) < 0.01: return True
        return False