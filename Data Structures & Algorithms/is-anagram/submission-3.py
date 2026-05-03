class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        d = {}
        e = {}
        
        for i in s:
            if i in d:
                d[i] += 1
            else:
                d[i] = 1

        for j in t:
            if j in e:
                e[j] += 1
            else:
                e[j] = 1

        return d == e