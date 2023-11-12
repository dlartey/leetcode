class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        # idea: go through each row and add it to a list, then sort it 
        # then get the index
        list1 = []
        for x in range(len(matrix)):
            list1.extend(matrix[x])
        
        return sorted(list1)[k-1]
        