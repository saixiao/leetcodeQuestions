class Solution:
    def numSplits(self, s: str) -> int:
        if len(s) == 0:
            return 0

        unique_right = 0
        right_chars = dict()
        
        for c in s:
            if c not in right_chars.keys():
                unique_right += 1
                right_chars[c] = 1
            else:
                right_chars[c] += 1
                
        unique_left = 0
        left_chars = set()
        
        res = 0
        for c in s:
            if c not in left_chars:
                unique_left += 1
                left_chars.add(c)
            right_chars[c] -= 1
            if right_chars[c] == 0:
                unique_right -= 1
            if unique_left == unique_right:
                res += 1
        
        return res