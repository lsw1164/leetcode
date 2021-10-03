class Solution:
    def integerBreak(self, n: int) -> int:
        if n == 2: return 1
        if n == 3: return 2
        cache = [None]*(n+1)
        cache[0], cache[1], cache[2] = 0, 1, 2
        
        def get_max_product(num):
            nonlocal cache
            if cache[num] != None: return cache[num]
            max_product = num
            for i in range(2, num//2 + 1):
                cur = get_max_product(i) * get_max_product(num - i)
                max_product = max(max_product, cur)
            cache[num] = max_product
            return max_product
                
        return get_max_product(n)