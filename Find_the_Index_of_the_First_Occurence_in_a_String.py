class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        i,j = 0,len(needle)
        for i in range(len(haystack)):
            if needle in haystack[i:j]:
                return i
            else:
                j += 1
        return -1