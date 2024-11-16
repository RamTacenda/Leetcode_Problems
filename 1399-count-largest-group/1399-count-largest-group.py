class Solution:
    def countLargestGroup(self, n: int) -> int:
        mapp = defaultdict(int)
        for i in range(1, n+1):
            if(str(i) == 1):
                mapp[i] += 1
            else:
                res = 0
                while(i > 0):
                    rem = i % 10
                    res += rem
                    i //= 10
                
                mapp[res] += 1

        groups = sorted(mapp.values(), reverse=True)
        return groups.count(max(groups))
