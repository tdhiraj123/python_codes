#Longest Palindromic Substring
'''
code with reduced time complex

Input: "babad"
Output: "bab"
Note: "aba" is also a valid answer.

'''

class Solution(object):
    def longestPalindrome(self, s):
        
        if(len(s)<1):
            return("")
        
        l=1
        ans=s[0]
        for i in range(0,len(s)):
            t=list(s)[i:]
            b=0
            while(len(t)>l and b<len(s)):
                b+=1
                j=len(t)-1-t[::-1].index(t[0])
                t=t[:j+1]
                if(t==t[::-1]):
                    if(len(t)>l):
                        l=len(t)
                        ans=t
                    
                    break
                t=t[:-1]
        return(''.join(ans))
                    
            
