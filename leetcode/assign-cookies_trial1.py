class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        childPtr = 0
        cookiePtr = 0
        contentChildren = 0
        while childPtr < len(g) and cookiePtr < len(s):
            greed = g[childPtr]
            size = s[cookiePtr]
            if size >= greed:
                contentChildren += 1
                childPtr += 1  
                cookiePtr += 1 
            else:
                cookiePtr += 1 
        return contentChildren