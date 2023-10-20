class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        # calculate equation for the line O(1)
        p1 = coordinates[0]
        p2 = coordinates[1]

        # slope = (y2-y1)/(x2-x1)
        # calculate the rate of slope change between different points from a reference point
        y1 = (p2[1]-p1[1])
        x1 = (p2[0]-p1[0])
        
        n = len(coordinates)
        
        # O(n) to iterate through the rest of the values
        for x in range(2,n):
            # O(1)
            if y1 * (coordinates[x][0] - p1[0]) != x1 * (coordinates[x][1] - p1[1]):
                return False

        return True
        # O(n) in total