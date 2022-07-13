class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        adict = {}
        s = list(s)
        t = list(t)
        for i in range(len(s)):
            if s[i] not in adict and t[i] not in adict:
                adict[s[i]] = t[i]
            else:
                if s[i] in adict and adict[s[i]] != t[i]:
                    return False
                if t[i] in adict and adict[t[i]] != s[i]:
                    return False
        return True

aaa = Solution()
bbb = aaa.isIsomorphic("paper","title")
pass