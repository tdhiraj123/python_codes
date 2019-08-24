# partial sorting array that is replacing with a element just greater element

l=list(map(int,input().split()))
f=[]
for i in range(len(l)-1):
    temp=max(l[i+1:])
    f.append(temp)
f.append(-1)
print(f)

'''
https://www.geeksforgeeks.org/replace-every-element-with-the-greatest-on-right-side/
'''
    

        
