class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        if len(nums) < 3:
            return max(nums)
        count = dict.fromkeys(nums,0)
        keys = []
        for j in count.keys():
            keys.append(j)
        if len(keys) < 3:
            return max(keys)
        return sorted(keys, reverse = True)[2]