class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        # Building hashmap
        mapp = dict()
        for i in range(0, len(s)):
            if(s[i] not in mapp):
                mapp[s[i]] = i
            else:
                mapp[s[i]] = i
        
        res = []
        start, end = 0, 0
        for i in range(0, len(s)):
            end = max(end, mapp[s[i]])
            if i == end:
                res.append(end-start+1)
                start = end+1

        return res