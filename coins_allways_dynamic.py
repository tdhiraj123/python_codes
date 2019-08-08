# no.of possible ways of making an amount, from given coins
amt = int(input('amount: '))
coin =list(map(int,input().split()))

dp=[[0 for _ in range(amt+1)] for _ in range(len(coin)+1)]

dp[0][0]=1
for i in range(1,len(coin)+1):

    dp[i][0]=1

    for j in range(1,amt+1):
        cv=coin[i-1]

        woc=dp[i-1][j]
        wc=0
        if(cv<=j):
            wc=dp[i][j-cv]
        dp[i][j]=woc+wc

print(dp)
        
'''
https://github.com/bephrem1/backtobackswe/blob/master/Dynamic%20Programming%2C%20Recursion%2C%20%26%20Backtracking/changeMakingProblem2.java
'''
