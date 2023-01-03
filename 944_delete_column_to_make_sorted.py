class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        res = 0
        for vals in zip(*strs):
            for actual, expected in zip(vals, sorted(vals)):
                if actual != expected:
                    res += 1
                    break
                    
        return res
