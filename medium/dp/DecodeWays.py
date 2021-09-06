class Solution:
    def numDecodings(self, s: str) -> int:
        if s[0] == "0":
            return 0
        
        look_behind_1 = 1
        look_behind_2 = 1
        
        # fib add
        for i in range(1, len(s)):
            current = 0
            if s[i] != "0":
                current = look_behind_1
            double_digit = int(s[i - 1] + s[i])
            if 10 <= double_digit <= 26:
                current += look_behind_2
            
            look_behind_2 = look_behind_1
            look_behind_1 = current
        
        return look_behind_1