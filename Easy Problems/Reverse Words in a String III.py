'''Runtime: 52 ms, faster than 27.18% of Python3 online submissions for Reverse Words in a String III.
   Memory Usage: 13.1 MB, less than 96.15% of Python3 online submissions for Reverse Words in a String III.
   '''

def reverseWords(s):
    '''type s = str
       :rtype = str
       '''
    words = s.split()
    for i in range(len(words)):
        words[i] = words[i][::-1]
    return " ".join(words)


print(reverseWords("Let's take LeetCode contest"))
