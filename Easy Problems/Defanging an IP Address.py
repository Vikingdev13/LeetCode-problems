# Time:  O(n)
# Space: O(1)

class Solution:
    def defangIPaddr(self, address):
        return address.replace('.', '[.]') if '.' in address else address
