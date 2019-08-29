'''
validating paraenthisis of the given string

Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

    Open brackets must be closed by the same type of brackets.
    Open brackets must be closed in the correct order.


Example 1:

Input: "()"
Output: true


'''

class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s=list(s)
        d={')':'(','}':'{',']':'['}
        if(len(s)==0):
            return True
        stack=[]
        for i in range(len(s)):
            if(s[i] in d):
                try:
                    if(d[s[i]]==stack[len(stack)-1]):
                        x=stack.pop()
                    else:
                        return(False)
                        
                except:
                    return(False)
            else:
                stack.append(s[i])
        if(len(stack)==0):
            return(True)
            
            
