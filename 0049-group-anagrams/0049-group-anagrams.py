class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        check = {chr(i+97) : i for i in range(0, 27)}

        for s in strs:
            count = [0]*(26)

            for c in s:
                count[check[c]] += 1

            res[tuple(count)].append(s)

        return list(res.values())