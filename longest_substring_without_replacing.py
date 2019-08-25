'''
Longest Substring Without Repeating Characters

Input: "abcabcbb"
Output: 3 
Explanation: The answer is "abc", with the length of 3. 

'''

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        ss=''
        m=0
        t=''
        for c in s:
            if len(ss)>m:
                m=len(ss)
                t=ss
            if c in ss:
                ss=ss[ss.index(c)+1:]
            
                
            ss=ss+c
        if(len(ss)>m):
            m=len(ss)
        return(m)
                

        
        
        
        
