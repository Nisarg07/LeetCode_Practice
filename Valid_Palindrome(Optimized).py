class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.replace(" ","")
        s = "".join(c for c in s if c.isalnum()).lower()
        start, end = 0,len(s)-1
        while start <= end:
            if s[start] == s[end]:
                start += 1
                end -= 1
            else:
                return False
        return True