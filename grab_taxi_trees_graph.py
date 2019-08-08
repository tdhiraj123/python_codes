# grab taxi 2019 question - trees question
'''
an array which represents the height of the trees will be given

to decorate the garden all the trees should be un and down i.e one should be tall
and the next one should be short and it be followed by a tall one again

if they are not in the requried order return by no.of ways they could be
decorated by cutting only one tree

if not possible return -1
if give trees are decorated return 0

e.g

input 3 4 5 3 7
o/p    3

input 4 5 6 3 7
output 2

input 1 2 3 4 5
o/p    -1

'''

tr=list(map(int,input('trees:').split()))
def sol(tr):

    ind=-1
    slop=[]
    for i in range(len(tr)-1):

        if(tr[i+1]-tr[i] <=0):
            slop.append(-1)
            
        else:
            slop.append(1)

    count=0
    for i in range(len(slop)-1):

        if((slop[i]==1 and slop[i+1]==1) or (slop[i]==-1 and slop[i+1]==-1)):
            
            count+=1
            ind=i
    return([ind,count])

ind,count=sol(tr)
if(count==0):
    print(0)
elif(count>1):
    print(-1)
else:
    f=0
    for i in range(3):
        copy_t=[]
        for j in tr:
            copy_t.append(j)
        dum=copy_t.pop(ind+i)
        z,p=sol(copy_t)
        if(p==0):
            f=f+1
    print(f)


