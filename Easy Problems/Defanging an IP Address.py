class Solution:
    def defangIPaddr(self, address: str) -> str:
            return address.replace('.', '[.]') if '.' in address else address