# question asked in tcs ninja 2019

x=input()
sum_odd=0
sum_even=0

for digits in range(len(x)):
    
    if (digits+1)%2==0:
        sum_even+=int(x[digits])
        
    else:
        sum_odd+=int(x[digits])
print(abs(sum_odd-sum_even))
