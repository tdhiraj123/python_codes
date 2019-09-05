# longest valid parentheses

def longestValidParentheses( s):
        """
        :type s: str
        :rtype: int
        """
        r=0
        s=list(s)
        stk=[-1]
        for i in range(len(s)):
            if(s[i]=='('):
                stk.append(i)
            else:
                stk.pop()
                if(len(stk) != 0):
                    r=max(r,i-stk[len(stk)-1])
                else:
                    stk.append(i)
        return r
print(longestValidParentheses('(((()()())'))
    
                    
    
