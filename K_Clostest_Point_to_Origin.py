import heapq

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        max_heap = []
        heapq.heapify(max_heap)
        for x,y in points:
            distance = x**2 + y**2
            item = [-distance,x,y]

            if len(max_heap) < k:
                heapq.heappush(max_heap,item)

            elif -distance > max_heap[0][0]:
                heapq.heapreplace(max_heap,item)

        return [[x,y] for (dis,x,y) in max_heap]