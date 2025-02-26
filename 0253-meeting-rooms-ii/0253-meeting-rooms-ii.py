class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        rooms = 0
        ans = 0
        events = [(a,1) for a,_ in intervals]
        events+= [(b,-1) for _,b in intervals]
        events.sort()
        for _,c in events:
            rooms+=c
            ans = max(ans, rooms)
        return ans