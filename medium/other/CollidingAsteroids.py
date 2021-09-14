class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack  = []
        
        for asteroid in asteroids:
            if asteroid > 0:
                stack.append(asteroid)
            if asteroid < 0:
                if len(stack) == 0 or stack[-1] < 0:
                    stack.append(asteroid)
                while len(stack) > 0 and stack[-1] > 0:
                    if abs(asteroid) == stack[-1]:
                        stack.pop()
                        break
                    elif abs(asteroid) > stack[-1]:
                        stack.pop()
                        if len(stack) == 0 or stack[-1] < 0:
                            stack.append(asteroid)
                            break
                    elif abs(asteroid) < stack[-1]:
                        break
        
        return stack