class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        if n == 1:
            return 1
        graph = defaultdict(list)
        trust_person = {}
        for u,v in trust:
            graph[v].append(u)
            trust_person[u] = 1
        for u in graph:
            if len(graph[u]) == n-1 and u not in trust_person:
                return u
        return -1
        