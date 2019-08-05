# solution for the question asked in tcs digital 2019
# bodmas in string
# input - 2+3*4-5

s = input('enter the input').split()
i=0
sum=0
while('mul' in s):

    i=s.index('mul')
    s[i]=int(s[i-1]) * int(s[i+1])
    x=s.pop(i+1)
    y=s.pop(i-1)

while('div' in s):

    i=s.index('div')
    s[i]=int(s[i-1])/int(s[i+1])
    x=s.pop(i+1)
    y=s.pop(i-1)

while('add' in s):

    i=s.index('add')
    s[i]=int(s[i-1]) + int(s[i+1])
    x=s.pop(i+1)
    y=s.pop(i-1)

while('sub' in s):

    i=s.index('sub')
    s[i]=int(s[i-1]) - int(s[i+1])
    x=s.pop(i+1)
    y=s.pop(i-1)

print(s)

    

    

    

    
