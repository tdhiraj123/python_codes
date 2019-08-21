# min cuts to make a parlindrome
'''
Given a string, a partitioning of the string is a palindrome partitioning
if every substring of the partition is a palindrome.

For example, “aba|b|bbabb|a|b|aba” is a palindrome
partitioning of “ababbbabbababa”.

Determine the fewest cuts needed for palindrome partitioning of a given string.

For example, minimum 3 cuts are needed for “ababbbabbababa”.
The three cuts are “a|babbbab|b|ababa”. If a string is palindrome,
then minimum 0 cuts are needed.

https://www.geeksforgeeks.org/palindrome-partitioning-dp-17/

'''
s=input('s:')
a=[[0 for _ in range(len(s)+1)]for _ in range(len(s)+1)]

for i in range(len(s)+1):
    a[0][i]=1000

for i in range(1,len(s)+1):
    for j in range(1,len(s)+1):

        x=1000

        if(j<i):
            x=a[i-1][j]
        elif(i==j):

            x=min(a[i-1][j],1+a[i][j-1])
            
        else:

            if(s[i-1:j]== s[i-1:j][::-1]):

                x=min(a[i-1][j],a[i][i-1]+1)
        
        a[i][j]=min(x,a[i-1][j])


print(a[len(s)][len(s)]-1)

            
