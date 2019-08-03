# difference of elements in a array

ar = list(map(int,input('enter elements').split()))

d=int(input('difference: '))

bol = False 
try:
    for i in range(0,len(ar)):

        for j in range(0,len(ar)):

            if(abs(ar[i]-ar[j]) == d):

                print(str(ar[i]) +"  "+str(ar[j]))

                raise Exception('done')

except Exception as e:

    print(e)

            
            

            
