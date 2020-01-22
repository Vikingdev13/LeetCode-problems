'''Runtime: 44 ms, faster than 6.07% of Python3 online submissions for Valid Parentheses.
Memory Usage: 12.6 MB, less than 100.00% of Python3 online submissions for Valid Parentheses.'''


class Solution:
    def isValid(self, s: str) -> bool:
        openBrackets = "([{"
        closeBrackets = ")]}"
        matchingBrackets = {')': '(', ']': '[', '}': '{'}
        stack = []

        for c in s:
            if c in openBrackets:
                stack.append(c)
            elif c in closeBrackets:
                if len(stack) == 0:
                    return False
                if stack[-1] == matchingBrackets[c]:
                    stack.pop()
                else:
                    return False
        return len(stack) == 0

'''Runtime: 56 ms, faster than 6.07% of Python3 online submissions for Valid Parentheses.
Memory Usage: 12.8 MB, less than 100.00% of Python3 online submissions for Valid Parentheses.'''

def is_matched(s):
    lefty = "([{"
    righty = ")]}"
    stack = []

    for c in s:
        if c in lefty:
            stack.append(c)
        elif c in righty:
            if len(stack) == 0:
                return False
            if righty.index(c) != lefty.index(stack.pop()):
                return False
    return len(stack) == 0

'''Runtime: 40 ms, faster than 10.57% of Python3 online submissions for Valid Parentheses.
Memory Usage: 12.8 MB, less than 100.00% of Python3 online submissions for Valid Parentheses'''

def is_matched2(s):
    lefty = "([{"
    righty = ")]}"
    stack = []

    for c in s:
        if c in lefty:
            stack.append(c)
        else:
            if len(stack) == 0:
                return False
            popped = stack.pop()
            if lefty.index(popped) != righty.index(c):
                return False
    return len(stack) == 0
