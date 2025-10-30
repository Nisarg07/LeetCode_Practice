class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i,j = 0,len(nums)-1
        while i < j or i == j:
            print(i,j)
            if nums[j] == val:
                j -= 1
            elif nums[i] == val:
                nums[i] = nums[j]
                i += 1
                j -= 1
            else:
                i += 1
        return i