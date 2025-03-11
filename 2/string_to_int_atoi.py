class Solution:
    def myAtoi(self, s: str) -> int:       
        INT_MIN = -2**31
        INT_MAX = 2**31 - 1
        
        s = s.lstrip()
        
        if not s:
            return 0
        
        sign = 1
        start_index = 0
        if s[0] == '-':
            sign = -1
            start_index = 1
        elif s[0] == '+':
            start_index = 1
        
        result = 0
        for i in range(start_index, len(s)):
            if not s[i].isdigit():
                break
            result = result * 10 + int(s[i])
        
        result *= sign
        
        if result < INT_MIN:
            return INT_MIN
        if result > INT_MAX:
            return INT_MAX
        
        return result
