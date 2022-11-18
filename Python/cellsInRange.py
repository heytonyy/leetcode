# https://leetcode.com/problems/cells-in-a-range-on-an-excel-sheet/


class Solution:
    def cellsInRange(self, s: str) -> List[str]:
        from string import ascii_uppercase
        d=dict()
        cells=list()
        for i in range(1,27):
            d[ascii_uppercase[i-1]]=i
        for c in range(d[s[0]],d[s[3]]+1):
            col = ''.join([k for k, v in d.items() if v == c])
            for r in range(int(s[1]),int(s[4])+1):
                cells.append(f'{col}{r}')
        return cells