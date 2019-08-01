# sabre question
# prime differnet combinations
# input - 5
'''
5 - 1 2 3 4 5
we to permutate all the prime and non-prime like

1 2 5 4 3
1 3 5 4 2
1 2 3 4 5
1 3 2 4 5
1 5 3 4 2
1 5 2 4 3

4 2 5 1 3
4 3 5 1 2
4 2 3 1 5
4 3 2 1 5
4 5 3 1 2
4 5 2 1 3

so ,there are totally '12' possible ways of doing it

output -12

'''
def isprime(n):

    b=False

    if(n==1):
        return b
    for i in range(2,(n//2)+1):

        if(n%i==0):
            return b
    else:
        return True
c=0
n=int(input('num:'))
for  i in range(1,n+1):

    if(isprime(i)):
        c+=1
p=1
for i in range(1,c+1):
    p=p*i
for j in range(1,(n-c)+1):
    p=p*j
print(p)
