class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        total = 0
        # when doing the minimum, update the index to have the max time
        prev = ""
        for i in range(len(colors)):
            if prev == "":
                prev = colors[i]
                continue

            current = colors[i]
            
            if prev == current:
                pt = neededTime[i-1]
                ct = neededTime[i]
                total+= min(pt,ct)

                # if the current isn't smaller, update it
                if (ct < pt):
                    neededTime[i] = pt
            prev = colors[i]

        return total
