class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        i = len(s) - 1
        j = 0        
        while(i > j or i == j):
            t = s[j]
            s[j] = s[i]
            s[i] = t
            i -= 1
            j += 1