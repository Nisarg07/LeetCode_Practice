import heapq

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = defaultdict(list)
        for u,v,w in times:
            graph[u].append([v,w])

        p_queue = [(0,k)]
        min_visit = {}

        while p_queue:
            time,u = heapq.heappop(p_queue)

            if u in min_visit:
                continue
            
            min_visit[u] = time

            for v,w in graph[u]:
                new_time = time + w
                heapq.heappush(p_queue,(new_time,v))

        if len(min_visit) == n:
            return max(min_visit.values())
        
        else:
            return -1
        