"""Runtime: 128 ms, faster than 67.17% of Python3 online submissions for Contains Duplicate.
   Memory Usage: 18.2 MB, less than 88.68% of Python3 online submissions for Contains Duplicate."""


def containsDuplicate(nums):
    '''
    :param nums: List[int]
    :return: bool
    '''
    return len(nums) != len(set(nums))


print(containsDuplicate([1, 2, 3, 4]))
