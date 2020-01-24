'''Runtime: 44 ms, faster than 5.58% of Python3 online submissions for Split a String in Balanced Strings.
   Memory Usage: 12.5 MB, less than 100.00% of Python3 online submissions for Split a String in Balanced Strings.
   '''


def balancedStringSplit(s):
    """
      :type s: str
      :rtype: int
    """
    count = 0
    result = 0
    for c in s:
        if c == 'R':
            count += 1
        else:
            count -= 1
        if count == 0:
            result += 1
    return result


print(balancedStringSplit("RLRRRLLRLL"))
