class Solution:
    def numSquares(self, n: int) -> int:
        # math soln, Adrien-Marie Legendre 3 square theorem
        def is_square(m):
            if m < 0:
                return False
            sq = int(math.sqrt(m))
            return sq*sq == m
        
        num = n
        
        while n & 3 == 0:
            n >>= 2
        if n & 7 == 7:
            return 4
        
        if is_square(num):
            return 1
    
        for i in range(1,int(num/2) + 1):
            if is_square(num - i*i):
                return 2
        return 3