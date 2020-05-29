p=[1,5,8,9,10,17,17,20,24,30] #Rod Prices
n=4 #Rod Length
r=[]
#Store calculated values in r
for i in range(n):
    r.append(-100)

def Cut_Rod_Memoized(p,n,r):
    q=-100
    if r[n-1]>=0:
        return r[n-1]
    if(n==0):
        q=0
    else:
        for i in range(0,n):
            #print(p[i],n-1-i)
            q=max(q,p[i]+Cut_Rod_Memoized(p[:n-i-i],(n-i-1),r)) #n-1 since array index starts at 0
    r[n-1] = q       
    return q
print("Maximum Revenue Obtainable is:",Cut_Rod_Memoized(p,n,r))