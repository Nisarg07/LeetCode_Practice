class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        m,n = len(s),len(p)
        ans = []
        if n > m:
            return []

        s_char = [0] * 26
        p_char = [0] * 26
        def char_to_index(c):
            return ord(c) - ord('a')
        for i in range(n):
            s_char[char_to_index(s[i])] += 1
            p_char[char_to_index(p[i])] += 1
        if s_char == p_char:
            ans.append(0)
        for end in range(n,m):
            char_in = s[end]
            char_out = s[end-n]

            s_char[char_to_index(char_in)] += 1
            s_char[char_to_index(char_out)] -= 1

            if s_char == p_char:
                ans.append(end-n+1)
        return ans