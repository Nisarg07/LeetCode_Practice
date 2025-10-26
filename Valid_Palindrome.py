class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.strip()
        s = s.lower()
        t = ""
        for c in s:
            if c.isalnum():
                t = t + c

        # print(t)
        # right, left = len(t) - 1, 0
        # while right > left or right == left:
        #     if t[right] == t[left]:
        #         right -= 1
        #         left += 1
        #         continue
        #     else:
        #         return False
        # return True
        return t == t[::-1]