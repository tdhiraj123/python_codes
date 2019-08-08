# microsoft 2019 - 10.5 l/annum question 
# parlindrome convertion
# given a string convert it into parlindrone by swapping elemints in string
# o/p return least no.of steps or swaps requried to convert
# sample input "ntiin"  o/p -- 1
# question is solved using greedy algo with a time complexity of O(n^2)

def parlin_conv(s,ar):
   
    c=0
    i=-1
    l=list(s)
    while((l[:len(l)//2] != (l[-len(l)//2:])[::-1]) and (i <(len(l)//2))):
        i+=1
        if(l[i]==l[len(l)-1-i]):
            pass
        elif((ar[ord(l[i])-97])%2 != 0):
            l[i],l[len(l)//2]=l[len(l)//2],l[i]
            c+=1
        else:
            
            x=l[i+1:].index(l[i])+i+1
            l[x],l[len(l)-1-i]=l[len(l)-1-i],l[x]
            c+=1
    return(c)
    

s=input('s:')
ar=[0 for _ in range(26)]
ls=s[:len(s)//2]
rs=s[-len(s)//2:]
rs=rs[::-1]
if(ls==rs):
    print(0)
uniq=0
for i in list(s):
    ar[ord(i)-97]+=1
cou=0
odd_count=0
for i in ar:

    if(i%2!=0 and i!=0):
        odd_count+=1
if((odd_count>1) or (odd_count==1 and len(s)%2 == 0)):
    print(-1)

else :
    print(parlin_conv(s,ar))
    
    

    

    
    

