class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        i = 0
        j = 0
        max_length = 0
        cur_length = 0
        exist = [False]*256
        while j < n:
            if not exist[ord(s[j])]:
                exist[ord(s[j])] = True
                j+=1
            else:
                while s[i] != s[j]:
                    exist[ord(s[i])] = False
                    i+=1
                i+=1
                j+=1
            cur_length = j - i
            max_length = max_length if max_length > cur_length else cur_length
        
        return max_length;
        
        
