class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        count = dict.fromkeys(nums,0)
        for i in nums:
            count[i] += 1
        print(count)
        for i in nums:
            while count[i] > 1:
                count[i] = count[i] - 1
                nums.remove(i)
        return len(nums)