class Solution(object):
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        mydict = dict()
        for i in range(len(nums)):
            diff = target - nums[i]
            if (diff in mydict):
                index = mydict[diff]
                return [index, i]
            else:
                mydict[nums[i]] = i
