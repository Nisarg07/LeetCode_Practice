class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_hash = {}
        for i, index in enumerate(nums):
            find = target - nums[i]

            if find in nums_hash:
                return [nums_hash[find],i]
            else:
                nums_hash[index] = i