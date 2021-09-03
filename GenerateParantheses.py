class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def generate(p, left, right, result):
            if left:
                generate(p + '(', left - 1, right, result)
            if right > left:
                generate(p + ')', left, right - 1, result)
            if not right:
                result.append(p)
        
        result = []
        generate("",n,n,result)
        return result