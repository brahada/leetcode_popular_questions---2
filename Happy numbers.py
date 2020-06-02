class Solution:
    def isHappy(self, n: int) -> bool:
        lookup = set()
        while True:
            if n in lookup: return False
            lookup.add(n)
            n = sum([int(i) ** 2 for i in str(n)])
            if n == 1: return True
