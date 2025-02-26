class Solution:
    def countSubstrings(self, s: str) -> int:
        count = 0
        for i in range(0, len(s)):
            temp = list()
            for j in range(i, len(s)):
                temp.append(s[j])
                if(temp == temp[::-1]):
                    count += 1
        return count