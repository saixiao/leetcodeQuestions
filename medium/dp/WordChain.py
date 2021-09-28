class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        def distance(long, short):
            for i in range(len(long)):
                if short in long[:i] + long[i+1:]:
                    return True
            return False
        
        word_sets = [set() for _ in range(17)]
        for w in words:
            word_sets[len(w) - 1].add(w)
        
        dp = {}
        res = 0
        for i in range(16, -1, -1):
            if len(word_sets[i]) == 0:
                dp = {}
                continue
            new_dp = {}
            for w in word_sets[i]:
                word_max = 0
                if len(dp.keys()) == 0:
                    new_dp[w] = 1
                for k in dp.keys():
                    if distance(k, w):
                        word_max = max(word_max, dp[k] + 1, word_max)
                        new_dp[w] = word_max
                    else:
                        new_dp[w] = max(1, word_max)

                res = max(res, max(list(new_dp.values())))
            dp = new_dp
        return res