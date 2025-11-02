class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        start,end = 0,k
        sum_nums = sum(nums[start:end])
        max_sum = sum_nums
        for i in range(k,len(nums)):
            sum_nums = sum_nums + nums[i] - nums[i-k]
            max_sum = max(sum_nums,max_sum)
            start += 1
            end += 1

        return max_sum/k