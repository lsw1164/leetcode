class Solution:
    def threeEqualParts(self, arr: List[int]) -> List[int]:
        total_num_of_one = sum(arr)
        
        if total_num_of_one == 0:
            return [0, len(arr)-1]
            
        if total_num_of_one % 3 != 0:
            return [-1, -1]
        num_of_one = total_num_of_one / 3
        
        
        one_cnt = 0
        
        first_delimiter = [1, num_of_one+1, 2*num_of_one+1]
        last_delimiter = [num_of_one, 2*num_of_one, 3*num_of_one]
        
        firsts, lasts = [], []
        for i in range(len(arr)):
            if arr[i] == 0: continue
            one_cnt += 1
            if one_cnt in first_delimiter:
                firsts.append(i)
            if one_cnt in last_delimiter:
                lasts.append(i)
        f1, f2, f3 = firsts 
        l1, l2, l3 = lasts
        
        if not arr[f1:l1+1] == arr[f2:l2+1] == arr[f3:l3+1]:
            return [-1, -1]
        
        x, y, z = f2-l1-1, f3-l2-1, len(arr)-l3-1
        if x < z or y < z:
            return [-1, -1]
        
        return [l1+z, l2+z+1]