from collections import Counter
from typing import List
class Solution:
    def minimumRounds(self, tasks: List[int]) -> int:
        rounds = 0
        for count in Counter(tasks).values():
            if count == 1:
                return -1
            iters, rem = divmod(count, 3)
            rounds += iters
            if rem > 0:
                rounds += 1
        return rounds 
