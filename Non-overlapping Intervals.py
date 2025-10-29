class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        count=0
        prevend=intervals[0][1]
        for start,end in intervals[1:]:
            if start>=prevend:
                prevend=end
            else:
                count+=1
                prevend=min(prevend,end)
        return count
        #TC:O(nlogn)
        #SC:O(1)--based on the sorting algo it may be O(n)

 
