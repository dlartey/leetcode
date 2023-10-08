class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        res = [[1],[1,1]]

        for x in range(1,rowIndex):
            temp = []
            temp.append(1)
            prev = res[-1]

            for x in range(len(prev)-1):
                temp.append(prev[x]+prev[x+1])
            temp.append(1)
            res.append(temp)
        return res[rowIndex]


        