class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        start = 0
        max_len = 0
        hash_set = {}
        for end in range(len(s)):
            cur_char = s[end]
            if cur_char in hash_set:
                index = hash_set[cur_char]
                start = max(start,index + 1)
            hash_set[cur_char] = end
            max_len = max(max_len, end-start+1)

        return max_len
        