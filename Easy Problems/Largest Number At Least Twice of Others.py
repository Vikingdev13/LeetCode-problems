class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        largest = max(nums)
        if all(largest >= 2*n for n in nums if n != largest):
            return nums.index(largest)
        return -1