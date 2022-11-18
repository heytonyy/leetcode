# https://leetcode.com/problems/count-items-matching-a-rule/

class Solution:
    def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
        d = {
          'type': [],
          'color': [],
          'name': []
        }
        for i in range(len(items)):
          d['type'].append(items[i][0])
          d['color'].append(items[i][1])
          d['name'].append(items[i][2])
        return len(list(filter(lambda v: v==ruleValue, d[ruleKey])))

        