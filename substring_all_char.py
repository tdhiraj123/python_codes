# minimum substring with all the elements of the string

s=input('s:')

def count(s):

    ar=[0 for _ in range(26)]
    for i in s:

        ar[ord(i)-97]+=1
        
    c=0
    for i in ar:

        if(i != 0):
            c+=1
    return(c)

sub_str=''
mi=s
c=count(s)
l=[]

for i in range(len(s)):
    for j in range(i+1,len(s)+1):

        sc=count(s[i:j])

        if(sc==c):

            l.append(len(s[i:j]))
            if(len(s[i:j])< len(mi)):
               mi=s[i:j]
print(min(l))
print(mi)
    
