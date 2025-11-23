import heapq

class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:

        n = len(points)
        adj = defaultdict(list)

        for i in range(n):
            for j in range(i+1,n):
                x1,y1 = points[i]
                x2,y2 = points[j]

                cost = abs(x1-x2) + abs(y1-y2)

                adj[i].append([cost,j])
                adj[j].append([cost,i])

        min_heap = [[0,0]]
        visited = {}
        min_cost = 0
        no_edges = 0

        while min_heap and no_edges < n:
            cost,u = heapq.heappop(min_heap)

            if u in visited:
                continue

            visited[u] = 1
            min_cost += cost
            no_edges += 1

            if no_edges == n:
                break

            for n_cost,v in adj[u]:
                if v not in visited:
                    heapq.heappush(min_heap,[n_cost,v])

        return min_cost