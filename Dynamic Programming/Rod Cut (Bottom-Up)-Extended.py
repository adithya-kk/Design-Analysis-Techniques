p=[1,5,8,9,10,17,17,20,24,30] #Rod Prices
n=10 #Rod Length
r=[] #revenue
s=[] #cuts to get max revenue

r=[0 for i in range(n+1)]
s=[0 for i in range(n+1)]

def Cut_Rod_Bottom_Up_Extended(p,n):
    for j in range(1,n+1):
        q=-100
        print("j:",j)
        for i in range(j):
            if(q<(p[i]+r[j-i-1])):
                q=p[i]+r[j-i-1] #n-1 since array index starts at 0
                s[j]=i+1
        r[j]=q 
        print("Current r[j]",r[j])
    return r,s,q



def Print_Cut_Rod_Solution_Extended(p,n):
        r,s,q= Cut_Rod_Bottom_Up_Extended(p,n)
        
        print("r[i] of "+str(r))
        print("s[j] of "+str(s))
        
        print("Maximum Revenue Obtainable is: ",q)
        while(n>0):
            print("Cut of "+str(s[n]))
            n=n-s[n]

Print_Cut_Rod_Solution_Extended(p,n)