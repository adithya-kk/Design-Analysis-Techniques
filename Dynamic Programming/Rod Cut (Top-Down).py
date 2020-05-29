p=[1,5,8,9,10,17,17,20,24,30] #Rod Prices
n=4 #Rod Length
def Cut_Rod(p,n):
    if(n==0):
        return 0
    else:
        q=-100
        for i in range(0,n):
            #print(p[i],n-1-i)
            q=max(q,p[i]+Cut_Rod(p,(n-1)-i)) #n-1 since array index starts at 0
            
        return q
print("Maximum Revenue Obtainable is:",Cut_Rod(p,n))

