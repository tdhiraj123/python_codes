s=list(input())

def  sol(s):

         ar=[0 for _ in range(26)]
         ar[ord(s[0])-97]+=1
         ar[ord(s[1])-97]+=1
         ar[ord(s[2])-97]+=1

         if(2 in ar) :
                  return chr(ar.index(2)+97)
         if(3 in ar):
                  return chr(ar.index(3)+97)
         else:
                  return s[2]+s[2]
while(len(s)>2):

         h=sol(s[:3])
         z=s.pop(0)
         if(len(h)==2):
                  s[0]=h[0]
                  s[1]=h[1]
         else:
                  z=s.pop(0)
                  s[0]=h
print(len(s))
print(s)
                  
