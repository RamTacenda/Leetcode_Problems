class Solution:
    def strStr(self, haystack: str, needle: str) -> int:

        if(needle in haystack):
            for i in range(0, len(haystack)):
                temp = []
                for j in range(i, len(haystack)):
                    temp.append([j, haystack[j]])
                    if(temp[0][1] == needle[0] and len(temp) == len(needle)):
                        computed = "".join([i[1] for i in temp])
                        if(computed == needle):
                            return temp[0][0]
        else:
            return -1