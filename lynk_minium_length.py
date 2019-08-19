# Lynk 2019
'''
minimum length of the string

the string contains repetation of characters x y and z
any 2 adjecent characters could be replaced by the third one
need the return the length of the final string

test-1
input - xyz
output- 2   - (xy)z -> zz

test-2
input - xyzy
o/p - 1   - (xy)zy -> z(zy) -> zx -> y

'''

s=list(input('enter the string:'))

i=0
l=len(s)
def left(s):
    ar=[0,0,0]
    ar[ord(s[0])-120]+=1
    ar[ord(s[1])-120]+=1
    return(chr(ar.index(0)+120))
while(len(s)>2):
    if(s[i]!=s[i+1]):
        a=left(s[i:i+2])
        t=s.pop(i)
        s[i]=a
    else:
        i=(i+1)%(len(s)-1)
if(len(s)==2):
    if(s[0]==s[1]):
        print(s)
        pass
    else:
        print(left(s))
else:
    print(s)
