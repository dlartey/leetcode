class Solution:
    def average(self, salary: List[int]) -> float:
        minSal = min(salary)
        maxSal = max(salary)
        count = 0
        res = 0
        for x in salary:
            if (x != minSal and x != maxSal):
                count+=1
                res+=x
        
        return res/count
        