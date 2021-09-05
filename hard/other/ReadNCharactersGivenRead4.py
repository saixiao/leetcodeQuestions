# The read4 API is already defined for you.
# def read4(buf4: List[str]) -> int:

class Solution:
    def __init__(self):
        self.buffer = []
    
    def read(self, buf: List[str], n: int) -> int:
        # read whole file
        if len(self.buffer) == 0:
            b = ["x"] * 4
            read4Res = read4(b)
            self.buffer = self.buffer + b[:read4Res]
            while read4Res > 0:
                b = ["x"] * 4
                read4Res = read4(b)
                self.buffer = self.buffer + b[:read4Res]
                
        poppedCount = 0
        
        while n > 0 and len(self.buffer) > 0:
            buf[poppedCount] = self.buffer.pop(0)
            n -= 1
            poppedCount += 1

        return poppedCount