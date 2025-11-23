class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        parent = list(range(n))

        def find(i):
            if parent[i] == i:
                return i
            
            parent[i] = find(parent[i])
            return parent[i]

        def union(i,j):
            root_i = find(i)
            root_j = find(j)

            if root_i != root_j:
                parent[root_j] = root_i
                return 1
            return 0

        for i in range(n):
            for j in range(i+1,n):
                if isConnected[i][j]:
                    union(i,j)

        count = 0
        for i in range(n):
            if parent[i] == i:
                count += 1

        return count
        