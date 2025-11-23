class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        parent = list(range(n))
        rank = [0] * n
        
        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        def union(x,y):
            root_x = find(x)
            root_y = find(y)

            if root_x != root_y:
                if rank[root_x] < rank[root_y]:
                    parent[root_x] = root_y
                elif rank[root_x] > rank[root_y]:
                    parent[root_y] = root_x
                else:
                    parent[root_x] = root_y
                    rank[root_x] += 1
                return True
            return False

        min_cost = 0
        no_edges = 0
        adj = []

        for i in range(n):
            for j in range(i+1,n):
                x1,y1 = points[i]
                x2,y2 = points[j]

                cost = abs(x1-x2) + abs(y1-y2)
                adj.append([cost,i,j])

        adj.sort()
        for cost,u,v in adj:
            if union(u,v):
                min_cost += cost
                no_edges += 1
            if no_edges == n-1:
                break

        return min_cost

        