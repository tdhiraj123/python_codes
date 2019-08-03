#array rotation

ar= list(map(int,input("enter the input array: ").split()))
r=input('rotation direction: ')
n=int(input('positions: '))

if(r == 'L'):

    for i in range(0,n):

        x=ar[i]
        ar.append(x)
        o=ar[n:]

else:

    f=[]

    for i in range(n-1,-1,-1):

        x=ar[len(ar)-1-i]
        f.append(x)

    o=f+ar[:n]

print(o[:len(ar)])

    

    
