from collections import Counter
from typing import List


class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        counter = Counter(arr)
        check_val = set()
        for i in counter:
            if counter[i] not in check_val:
                check_val.add(counter[i])
            else:
                return False
        return True

class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        count = Counter(arr)
        mylist = []
        for key, val in count.items():
            mylist.append(val)
        if len(mylist) == len(set(mylist)):
            return True
        return False
