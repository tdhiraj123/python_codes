'''
converting a integer to roman value

Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000

Input: 58
Output: "LVIII"
Explanation: L = 50, V = 5, III = 3.

'''



class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        n=num
        f=''
        d={1:'I',5:'V',10:'X',50:'L',100:'C',500:'D',1000:'M'}
        c=0
        while(n>0):
            x=n%10*(10**c)
            
            if(x/(10**c)<4):
                f=((d[10**c])*(x/(10**c)))+f
            
            elif(x/(10**c)==4):
                
                f=(d[10**c]+d[5*(10**c)])+f
                
            elif(x/(10**c)<9):
                f=(d[5*(10**c)]+((x/(10**c))-5)*d[10**c])+f
                
            elif(x/(10**c)==9):
                f=(d[10**c]+d[10**(c+1)])+f
                
            n=n//10
            c+=1
        return f
                
            
            
