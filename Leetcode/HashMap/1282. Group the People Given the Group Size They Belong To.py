class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        res = []
        groupMap = collections.defaultdict(list)
        
        for i,x in enumerate(groupSizes):
            if not x in groupMap or (x in groupMap and len(groupMap[x]) == 0):
                groupMap[x].append([])

            groupMap[x][-1].append(i)

            if (len(groupMap[x][-1]) == x):
                group = groupMap[x].pop()
                res.append(group)
        return res
        