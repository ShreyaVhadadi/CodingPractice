class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        hashmap={}
        for src,dest,time in times:
            if src not in hashmap:
                hashmap[src]=[]
            hashmap[src].append((dest,time))
        heap=[]
        heapq.heappush(heap,(0,k))
        maxtime=0
        visited=set()
        while heap:
            t1,n1=heapq.heappop(heap)
            if n1 in visited:
                continue
            visited.add(n1)  
            maxtime=max(t1,maxtime)      

            for n2,t2 in hashmap.get(n1,[]):
                if n2 not in visited:
                    heapq.heappush(heap,(t1+t2,n2))
        return maxtime if len(visited)==n else -1
        # TC:O(ElogV)
        #SC:O(E+V)

                





