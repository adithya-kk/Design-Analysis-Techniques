p=[1,5,8,9,10,17,17,20,24,30] #Rod Prices
n=4 #Rod Length
r=[] #revenue
#Store calculated values in r
r=[0 for i in range(n+1)]

def Cut_Rod_Bottom_Up(p,n):
        
    for j in range(1,n+1):
        q=-100
        print("j:",j)
        for i in range(j):
            print("Checking revenue between",q," j = ",j," i = ",i," j-i-1 = ",j-i-1)
            print("Price=",p[i],"r[j-i-1] = ",r[j-i-1])
            q=max(q,p[i]+r[j-i-1]) #n-1 since array index starts at 0
        r[j]=q 
        print("Current r[j]",r[j])
    return r[n]
print("Maximum Revenue Obtainable is:",Cut_Rod_Bottom_Up(p,n))