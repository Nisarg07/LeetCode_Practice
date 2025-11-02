class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        start, sum_nums = 0, 0
        arr_len = 999999
        for end in range(len(nums)):
            sum_nums += nums[end]

            while sum_nums >= target:
                arr_len = min(arr_len,end-start+1)
                sum_nums -= nums[start]
                start += 1

        return arr_len if arr_len != 999999 else 0