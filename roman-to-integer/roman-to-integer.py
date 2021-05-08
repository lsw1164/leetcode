class Solution:
    def romanToInt(self, s: str) -> int:
        
        roman_to_int = {
            "IV" : 4, "IX" : 9,  
            "XL" : 40, "XC" : 90,  
            "CD" : 400, "CM" : 900,
            "I" : 1, "V" : 5, 
            "X" : 10, "L" : 50, 
            "C" : 100, "D" : 500, 
            "M" : 1000
        }
        
        ans, i = 0, 0
        while i < len(s):
            if i < len(s) - 1 and s[i:i+2] in roman_to_int:
                ans += roman_to_int[s[i:i+2]]
                i += 2
                continue
            ans += roman_to_int[s[i]]
            i += 1
        return ans
            
        