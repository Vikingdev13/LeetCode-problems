from functools import reduce

class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        return reduce(lambda s, x: s + (1 - len(str(x)) % 2), nums, 0)