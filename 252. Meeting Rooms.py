class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        # sort the intervals
        end = -1
        intervals.sort()
        for i in intervals:
            if end == -1:
                end = i[1]
                continue
            
            if end <= i[0]:
                end = i[1]
            else:
                return False
        return True