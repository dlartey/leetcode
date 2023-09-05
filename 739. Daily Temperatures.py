class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # use hashmap and stack
        dicti = {}
        stack = []
        ans = []
        for i,temp in enumerate(temperatures):
            if (len(stack) == 0):
                stack.append((temp,i))
            else:
                while (temp > stack[-1][0]):
                    index = stack[-1][1]
                    dicti[index] = i-index
                    stack.pop()
                    if (len(stack) == 0):
                        break
                stack.append((temp,i))

        for x in range(len(temperatures)):
            if x in dicti:
                ans.append(dicti[x])
            else:
                ans.append(0)
                
        return(ans)