'''
maximum sum in a array such that no two elements are adjecent
'''

l=list(map(int,input('l:').split()))
inc=0 # sum including present element
exl=0 # maximum sum excluding present element
for num in l:
    x=max(inc,exl)
    inc=num+exl
    exl=x
print(max(exl,inc))
