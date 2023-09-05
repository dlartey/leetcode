class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pairs = sorted([(p,s) for p,s in zip(position,speed)])
        
        stack = []
        for i in range(len(pairs)-1,-1,-1):
            current = pairs[i]
            stack.append((target-current[0])/current[1])
            if (len(stack) > 1 and stack[-1] <= stack[-2]):
                stack.pop()
        
        return len(stack)
        