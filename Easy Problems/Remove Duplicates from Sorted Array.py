'''Runtime: 84 ms, faster than 77.42% of Python3 online submissions for Remove Duplicates from Sorted Array.
   Memory Usage: 14.5 MB, less than 97.54% of Python3 online submissions for Remove Duplicates from Sorted Array.'''


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        index = 0
        for i in range(1, len(nums)):
            if nums[index] != nums[i]:
                nums[index + 1] = nums[i]
                index += 1
        return index + 1