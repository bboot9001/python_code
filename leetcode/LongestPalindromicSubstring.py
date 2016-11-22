class Solution(object):
    def ExpandString(self,str1,left,right):
        nLen = len(str1)
        while left >= 0 and right <= nLen - 1 and str1[left] == str1[right]:
            left-=1
            right+=1
        
        return str1[left +1:right]
        
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        nLen = len(s)
        if nLen == 0:
            return ""
        
        MaxStr = s[0:1]
        for i in range(nLen):
            CurStr = self.ExpandString(s,i,i)
            if len(CurStr) > len(MaxStr):
                MaxStr = CurStr
            CurStr = self.ExpandString(s,i,i+1)
            if len(CurStr) > len(MaxStr):
                MaxStr = CurStr
        
        return MaxStr